from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # <-- NUEVA IMPORTACIÓN
from pydantic import BaseModel

app = FastAPI()

# <-- NUEVO BLOQUE DE CONFIGURACIÓN CORS:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite que tu página web se conecte desde cualquier lado
    allow_credentials=True,
    allow_methods=["*"], # Permite usar POST, GET, etc.
    allow_headers=["*"],
)


class MensajeUsuario(BaseModel):
    mensaje: str

def obtener_respuesta_ia(mensaje_usuario: str):
    mensaje = mensaje_usuario.lower()
    
    if "hola" in mensaje or "buenos" in mensaje or "buenas" in mensaje:
        return "¡Hola! Bienvenido a Lysifix. Soy tu asistente virtual. ¿En qué te puedo ayudar hoy? 😊"
        
    elif "precio" in mensaje or "costo" in mensaje or "cuanto cuesta" in mensaje or "cotizacion" in mensaje:
        return "Por seguridad y para darte una atención personalizada, manejamos todas nuestras cotizaciones y contrataciones directamente a través de nuestra plataforma oficial."
        
    elif "servicios" in mensaje or "que hacen" in mensaje or "desarrollo" in mensaje or "crean" in mensaje:
        return "En Lysifix nos especializamos en Desarrollo Web y Software a la medida. Creamos páginas web, aplicaciones y soluciones digitales profesionales."
        
    elif "contacto" in mensaje or "telefono" in mensaje or "correo" in mensaje:
        return "Puedes dejarnos un mensaje en la sección de 'Contacto' de esta página o escribirnos directamente a nuestro correo oficial."
        
    else:
        return "Disculpa, todavía estoy aprendiendo y no entendí tu pregunta. ¿Podrías intentar preguntar de otra forma?"

@app.post("/chat")
async def chat_endpoint(datos: MensajeUsuario):
    if not datos.mensaje or not datos.mensaje.strip():
        return {"respuesta": "El mensaje no puede estar vacío"}
        
    respuesta_bot = obtener_respuesta_ia(datos.mensaje)
    return {"respuesta": respuesta_bot}
