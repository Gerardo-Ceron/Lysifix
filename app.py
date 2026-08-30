from fastapi import FastAPI
from fastapi.responses import HTMLResponse # <-- AGREGA ESTA NUEVA IMPORTACIÓN
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

# ==========================================
# 1. RUTA NUEVA: Muestra tu página web al inicio
# ==========================================
@app.get("/", response_class=HTMLResponse)
async def home():
    try:
        # Lee tu archivo index.html automáticamente desde la raíz
        with open("index.html", "r", encoding="utf-8") as archivo:
            return archivo.read()
    except Exception as e:
        return "<h1>Error: No se encontró el archivo index.html en el servidor</h1>"

# ==========================================
# Todo lo demás de tu código lo dejas IGUAL abajo:
# ==========================================
class MensajeUsuario(BaseModel):
    mensaje: str

def obtener_respuesta_ia(mensaje_usuario: str):
    # ... (aquí van tus IF/ELIF del bot, déjalos como están)
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
