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
    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": instrucciones_asistente
            },
            {
                "role": "user",
                "content": mensaje_usuario
            }
        ]
    )
    return respuesta.choices.message.content