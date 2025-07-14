from PIL import ImageGrab
import pytesseract
import time
import requests

#Variables base
SUBTITLE_REGION = (530, 842, 1160, 1168)

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.1:8b"


last_text = ""

def traducir(texto):
   prompt = f"Por favor traduce este texto del inglés al español, solo dame la traducción: {texto}"
   response = requests.post(
      OLLAMA_URL,
      json={
         "model": OLLAMA_MODEL,
         "prompt": prompt
      }
   )
   data = response.json()
   return data["response"]
   

print("Iniciando OCR + traducción.... Ctrl+C para salir.\n")

while True:
    img = ImageGrab.grab(bbox=SUBTITLE_REGION)
    text = pytesseract.image_to_string(img).strip()

    if text and text != last_text:
        print(f"\n📝 Texto detectado: {text}")
        trad = traducir(text)
        print(f"🌍 Traducción: {trad}")
        last_text = text

    time.sleep(1)

