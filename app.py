from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq

app = FastAPI()

# Permite que tu página web se conecte al backend de Python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # En producción, cambia "" por el dominio de tu web
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key="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")

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
    respuesta = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": INFORMACION_EMPRESA},
            {"role": "user", "content": mensaje.texto}
        ],
        temperature=0.3 # Valores bajos hacen que la IA sea más precisa y no invente datos
    )
    return {"respuesta": respuesta.choices.message.content}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8500)