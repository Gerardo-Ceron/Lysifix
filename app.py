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

# ESTA ES LA FUNCIÓN QUE HACE QUE JALE TU PÁGINA WEB VISUAL
@app.get("/", response_class=HTMLResponse)
async def home():
    html_contenido = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Lysifix</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f9; margin: 0; padding: 20px; }
            h1 { color: #1a73e8; }
        </style>
    </head>
    <body>
        <h1>Bienvenido a Lysifix</h1>
        <p>Tu sitio web está en línea y el chat está listo.</p>
        
        <!-- Contenedor del Chat -->
        <div id="chat-contenedor" style="margin-top: 20px;">
            <div id="historial" style="border: 1px solid #ccc; height: 200px; padding: 10px; overflow-y: auto; background: white; margin-bottom: 10px;"></div>
            <input type="text" id="entrada" placeholder="Escribe tu duda aquí..." style="padding: 8px; width: 250px;">
            <button onclick="enviarMensaje()" style="padding: 8px 15px; background: #1a73e8; color: white; border: none; cursor: pointer;">Enviar</button>
        </div>

        <script>
        async function enviarMensaje() {
            const inputEntrada = document.getElementById("entrada");
            const historial = document.getElementById("historial");
            const textoUsuario = inputEntrada.value.trim();

            if (textoUsuario === "") return;

            historial.innerHTML += <div><b>Tú:</b> ${textoUsuario}</div>;
            inputEntrada.value = ""; 

            try {
                const respuesta = await fetch("https://lysifix.dev", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ "mensaje": textoUsuario })
                });
                const datos = await respuesta.json();
                historial.innerHTML += <div style="color: blue;"><b>Bot:</b> ${datos.respuesta}</div>;
                historial.scrollTop = historial.scrollHeight;
            } catch (error) {
                historial.innerHTML += <div style="color: red;">Error al conectar con el asistente.</div>;
            }
        }
        </script>
    </body>
    </html>
    """
    return html_contenido

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
