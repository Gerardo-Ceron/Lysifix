import os
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


def obtener_respuesta_ia(mensaje_usuario):
    # Convertimos el mensaje a minúsculas para que no importen las mayúsculas
    mensaje = mensaje_usuario.lower()
    
    # 1. Respuestas a saludos
    if "hola" in mensaje or "buenos dias" in mensaje or "buenas tardes" in mensaje:
        return "¡Hola! Bienvenido a Lysifix. Soy tu asistente virtual. ¿En qué te puedo ayudar hoy? 😊"
        
    # 2. Respuestas sobre precios o costos
    elif "precio" in mensaje or "costo" in mensaje or "cuanto cuesta" in mensaje or "cotizacion" in mensaje:
        return "Por seguridad y para darte una atención personalizada, manejamos todas nuestras cotizaciones y contrataciones directamente a través de nuestra plataforma oficial."
        
    # 3. Respuestas sobre servicios o qué hace la página
    elif "servicios" in mensaje or "que hacen" in mensaje or "desarrollo" in mensaje or "crean" in mensaje:
        return "En Lysifix nos especializamos en Desarrollo Web y Software a la medida. Creamos páginas web, aplicaciones y soluciones digitales profesionales."
        
    # 4. Información de contacto
    elif "contacto" in mensaje or "telefono" in mensaje or "correo" in mensaje:
        return "Puedes dejarnos un mensaje en la sección de 'Contacto' de esta página o escribirnos directamente a nuestro correo oficial."
        
    # 5. Respuesta por defecto si el bot no entiende la pregunta
    else:
        return "Disculpa, todavía estoy aprendiendo y no entendí tu pregunta. ¿Podrías intentar preguntar de otra forma o consultar nuestra sección de servicios?"

@app.post("/chat")
async def chat_endpoint(datos: MensajeUsuario):
    if not datos.mensaje.strip():
        return {"respuesta": "Disculpa, el mensaje no puede estar vacío."}
        
    respuesta_bot = obtener_respuesta_ia(datos.mensaje)
    return {"respuesta": respuesta_bot}
