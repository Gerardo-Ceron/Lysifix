import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
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

# 1. RUTA PARA JALAR TU PORTAFOLIO VISUAL COMPLETO
@app.get("/", response_class=HTMLResponse)
async def home():
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as archivo:
            return archivo.read()
    return "<h1>Lysifix: Servidor activo</h1>"

# 2. EL CONECTOR DEL CHAT (Mantiene tu bot inteligente)
class MensajeUsuario(BaseModel):
    message: str

def obtener_respuesta_ia(mensaje_usuario: str):
    mensaje = mensaje_usuario.lower()
    if "hola" in mensaje or "buenos" in mensaje or "buenas" in mensaje:
        return "¡Hola! Bienvenido a Lysifix. ¿En qué te puedo ayudar hoy? 😊"
    elif "precio" in mensaje or "costo" in mensaje or "cuanto cuesta" in mensaje or "cotizacion" in mensaje:
        return "Por seguridad y para darte una atención personalizada, manejamos todas nuestras cotizaciones y contrataciones directamente en Fiverr."
    elif "servicios" in mensaje or "que hacen" in mensaje or "desarrollo" in mensaje or "crean" in mensaje:
        return "En Lysifix nos especializamos en Desarrollo Web y Software a la medida. Creamos páginas web, aplicaciones y soluciones digitales profesionales."
    elif "contacto" in mensaje or "telefono" in mensaje or "correo" in mensaje:
        return "Puedes dejarnos un mensaje en la sección de 'Contacto' de esta página."
    else:
        return "Disculpa, todavía estoy aprendiendo y no entendí tu pregunta. ¿Podrías intentar preguntar de otra forma?"

@app.post("/chat")
async def chat_endpoint(datos: MensajeUsuario):
    if not datos.message or not datos.message.strip():
        return {"respuesta": "El mensaje no puede estar vacío"}
    respuesta_bot = obtener_respuesta_ia(datos.message)
    return {"respuesta": respuesta_bot}

# 3. TRUCO FINAL DE FASTAPI: Sirve todas tus carpetas (css, img, assets) de forma nativa
# Va hasta el final del archivo para que no tape las rutas del chat
app.mount("/", StaticFiles(directory=".", html=True), name="static")
