import pytesseract
import requests
import time
from PIL import ImageGrab

# Coordenadas de la región de subtítulos: (left, top, right, bottom)
SUBTITLE_REGION = (530, 842, 1160, 1168)

# Configura Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.1:8b"

def traducir(texto):
    # Limita longitud para evitar romper runner
    texto = texto.strip().replace('\n', ' ')
    if len(texto) > 500:
        texto = texto[:500]

    # Prompt claro y directo
    prompt = f"Traduce del inglés al español el siguiente texto. Solo devuelve la traducción, sin explicaciones:\n\n{texto}"
    print("\n🔹 Prompt enviado a Ollama:\n", prompt)

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
        print("🔍 Respuesta de Ollama:", data)

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

    while True:
        # Captura imagen de la zona definida
        img = ImageGrab.grab(bbox=SUBTITLE_REGION)
        text = pytesseract.image_to_string(img, lang='eng').strip()

        # Solo traduce si el texto cambió y no está vacío
        if text and text != ultimo_texto:
            print("\n📝 Texto detectado:\n", text)
            trad = traducir(text)
            print("🌍 Traducción:", trad)
            ultimo_texto = text

        time.sleep(1)  # Evita sobrecargar CPU y Ollama

if __name__ == "__main__":
    main()