import os
from openai import OpenAI

# Inicializamos el cliente de OpenAI de forma correcta
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

instrucciones_asistente = """
Eres el asistente virtual oficial de Lysifix (Desarrollo Web y Software). 
Tu objetivo es atender a los visitantes del portafolio, ser amable, profesional y hablar un español 100% perfecto de México. Está estrictamente prohibido usar Spanglish o mezclar inglés.

Sigue estas reglas de oro:
1. SALUDO CORDIAL: Cuando te digan "Hola", responde de forma breve, entusiasta y ofrece ayuda para sus proyectos.
2. CERO CHORO MAREADOR: Da respuestas cortas, directas y de menos de 3 líneas. Ve directo al grano.
3. FILTRO DE CONTRATACIÓN: Si preguntan por precios o contratar, diles amablemente que por seguridad manejamos todo mediante Fiverr, y dales el enlace oficial.
4. Si no sabes algo, di amablemente que eres un asistente en entrenamiento y que te contacten por Fiverr.
"""

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