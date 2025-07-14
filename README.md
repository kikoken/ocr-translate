# 📝 OCR + Traducción en tiempo real de subtítulos (Mac)

Este pequeño script en Python captura en tiempo real los subtítulos que aparecen en la pantalla (por ejemplo en reuniones de Teams o Google Meet), los traduce automáticamente del inglés al español usando un modelo local de Ollama y muestra el resultado por terminal.

Todo el proceso ocurre de forma **local**, sin enviar datos a servicios externos.

---

## ⚙️ Requisitos

- macOS
- Python 3.8 o superior
- [Tesseract OCR](https://tesseract-ocr.github.io/) (motor OCR)
- [Ollama](https://ollama.com/) instalado y corriendo localmente con al menos un modelo (ejemplo: `llama3.1:8b`)

---

## 📦 Instalación

1. **Clona o descarga el repositorio**:
```bash
git clone https://github.com/tu-usuario/ocr-translate-subtitles.git
cd ocr-translate-subtitles

2.	Instala dependencias de Python:
```bash
pip3 install -r requirements.txt
```

3.	Instala Tesseract OCR (una vez):
```bash
brew install tesseract
```

🛠 Configuración rápida
Edita el archivo ocr_translate.py y ajusta esta línea con las coordenadas exactas donde salen tus subtítulos en pantalla:

```python
SUBTITLE_REGION = (530, 842, 1160, 1168)
```
(Las coordenadas son: izquierda, arriba, derecha, abajo)

## 🚀 Uso

Inicia el script:
```bash
python3 ocr_translate.py
```
Verás en terminal algo así cuando detecta texto nuevo:

```
📝 Texto detectado: The quick brown fox jumps over the lazy dog.
🌍 Traducción: El rápido zorro marrón salta sobre el perro perezoso.
```
## 🧠 Cómo funciona
	•	Captura cada segundo una zona de la pantalla.
	•	Extrae texto con OCR (pytesseract).
	•	Envía el texto a Ollama para traducirlo del inglés al español.
	•	Imprime por terminal la traducción.
