import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# RUTA PRINCIPAL CON PARÁMETROS SEGUROS
@app.get("/", response_class=HTMLResponse)
async def home():
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as archivo:
            return archivo.read()
    return "<h1>Lysifix: Servidor activo, pero no se encontró tu archivo index.html</h1>"

# Reemplaza la función "servir_archivos_locales" por esta versión avanzada:
@app.get("/{archivo_nombre:path}")
async def servir_archivos_locales(archivo_nombre: str):
    # Primero busca en la raíz
    if os.path.exists(archivo_nombre):
        return FileResponse(archivo_nombre)
        
    # Si no lo encuentra, busca de forma inteligente en subcarpetas comunes
    carpetas_comunes = ["css", "img", "assets", "public", "images", "js"]
    for carpeta in carpetas_comunes:
        ruta_inteligente = os.path.join(carpeta, archivo_nombre)
        if os.path.exists(ruta_inteligente):
            return FileResponse(ruta_inteligente)
            
    return HTMLResponse(status_code=404)

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
