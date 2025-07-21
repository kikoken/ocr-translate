import pytesseract
import requests
import time
import json
import os
import gc
from PIL import ImageGrab

# Carga configuración desde archivo externo
def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        # Configuración por defecto si no existe el archivo
        return {
            "translation_prompt": "Traduce este texto del inglés al español. Mantén nombres propios y términos técnicos sin cambiar:",
            "subtitle_region": [530, 842, 1160, 1168],
            "ollama_url": "http://localhost:11434/api/generate",
            "ollama_model": "llama3.1:8b",
            "max_text_length": 500
        }

# Carga configuración
config = load_config()
SUBTITLE_REGION = tuple(config["subtitle_region"])
OLLAMA_URL = config["ollama_url"]
OLLAMA_MODEL = config["ollama_model"]

def traducir(texto):
    # Limita longitud para evitar romper runner
    texto = texto.strip().replace('\n', ' ')
    max_length = config.get("max_text_length", 500)
    if len(texto) > max_length:
        texto = texto[:max_length]

    # Usa el prompt de configuración
    translation_prompt = config.get("translation_prompt", "Traduce este texto del inglés al español:")
    prompt = f"""{translation_prompt}

{texto}"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            }
        )
        
        if response.status_code != 200:
            print(f"❌ Error HTTP {response.status_code}: {response.text}")
            return "[Error en traducción]"
        
        data = response.json()

        if "response" in data and data["response"].strip():
            return data["response"].strip()
        else:
            print("⚠️ Respuesta inesperada o vacía de Ollama:", data)
            return "[Traducción no disponible]"

    except Exception as e:
        print("❌ Error al llamar a Ollama:", e)
        return "[Error en traducción]"

def main():
    print("Iniciando OCR + traducción en terminal... Ctrl+C para salir.\n")
    ultimo_texto = ""
    iteration_count = 0

    while True:
        # Captura imagen de la zona definida
        img = ImageGrab.grab(bbox=SUBTITLE_REGION)
        try:
            text = pytesseract.image_to_string(img, lang='eng').strip()
        finally:
            # Limpia la imagen de memoria inmediatamente
            del img

        # Solo traduce si el texto cambió y no está vacío
        if text and text != ultimo_texto:
            trad = traducir(text)
            print("🌍 Traducción:", trad)
            ultimo_texto = text

        # Fuerza garbage collection cada 30 iteraciones (30 segundos)
        iteration_count += 1
        if iteration_count % 30 == 0:
            gc.collect()
            iteration_count = 0

        time.sleep(1)  # Evita sobrecargar CPU y Ollama

if __name__ == "__main__":
    main()