import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from pydantic import BaseModel
from groq import Groq


def cargar_entorno():
    archivo_env = Path(__file__).with_name(".env")
    if not archivo_env.exists():
        return

    for linea in archivo_env.read_text(encoding="utf-8").splitlines():
        linea = linea.strip()
        if linea and not linea.startswith("#") and "=" in linea:
            nombre, valor = linea.split("=", 1)
            os.environ.setdefault(nombre.strip(), valor.strip().strip('"\''))


cargar_entorno()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite conectar desde cualquier puerto local
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MensajeUsuario(BaseModel):
    texto: str

# Aquí configuras las Preguntas Frecuentes de tu negocio
INFORMACION_EMPRESA = """
Eres el asistente virtual inteligente de Lysifix, una agencia experta en desarrollo de software a la medida. 
Tu objetivo es resolver dudas de los clientes de forma profesional y guiarlos a contratarnos en Fiverr.

Usa la siguiente información para responder:
- Tecnologías: Desarrollamos software de alta calidad usando Python, JavaScript, React, FastAPI y soluciones avanzadas con Inteligencia Artificial.
- Tiempos de entrega: Los proyectos pequeños toman de 1 a 2 semanas. Proyectos más grandes dependen de la complejidad.
- Horarios de atención: Atendemos de Lunes a Viernes de 9:00 AM a 6:00 PM.
- Seguridad y Contratación: Por seguridad del cliente y de nuestra agencia, NO aceptamos pagos directos ni contratos por fuera. Todo el proceso de cotización, pago en garantía y entrega se gestiona exclusivamente a través de nuestro perfil oficial de Fiverr.

Enlace oficial de Fiverr para contrataciones: https://fiverr.com

Regla de oro: Si un cliente te pregunta por precios exactos, presupuestos o dice que quiere iniciar un proyecto, explícale la política de seguridad y proporciónale amablemente el enlace de Fiverr para que nos envíe un mensaje directo por allá. Si te preguntan algo que no sabes, diles que dejen su duda en nuestro buzón de Fiverr.
"""

@app.post("/chat")
async def chat_endpoint(mensaje: MensajeUsuario):
    texto = mensaje.texto.strip()
    if not texto:
        raise HTTPException(status_code=422, detail="Escribe una pregunta antes de enviar el mensaje.")

    try:
      
        cliente = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        
        respuesta = cliente.chat.completions.create(
           model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": INFORMACION_EMPRESA},
                {"role": "user", "content": mensaje.texto}
            ],
            temperature=0.3
        )
        return {"respuesta": respuesta.choices.message.content}

    except Exception as error:
        print(f"Error de Groq: {error}")
        raise HTTPException(status_code=502, detail="El proveedor de IA no pudo responder.") from error

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8500)

    