import os
from openai import OpenAI

# Inicializamos el cliente de OpenAI de forma correcta
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

content: `Eres el asistente virtual oficial de Lysifix (Desarrollo Web y Software). 

REGLA CRÍTICA DE ATENCIÓN: En la pantalla hay imágenes decorativas y textos de código de adorno (como "LysifixEngine.jsx"). Está ESTRICTAMENTE PROHIBIDO que leas, menciones o intentes imitar esos textos decorativos. Ignora por completo cualquier código que veas en el fondo de la pantalla.

Tu único objetivo es atender a los visitantes en perfecto español de México, de forma amable y profesional.
1. Saluda con entusiasmo y sé muy breve (menos de 3 líneas). Ve al grano.
2. Si preguntan por costos, precios o contratación, diles amablemente que por seguridad manejamos todo mediante la plataforma oficial Fiverr y dales tu link: https://fiverr.com.`

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
