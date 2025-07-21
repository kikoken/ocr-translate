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

## 🛠 Configuración

### Archivo de configuración

El script usa un archivo `config.json` para personalizar su comportamiento. Este archivo **no se incluye en el repositorio** para mantener tu configuración privada y ajustable.

Crea un archivo `config.json` en el directorio raíz del proyecto con el siguiente contenido:

```json
{
  "translation_prompt": "Traduce este texto del inglés al español. Mantén nombres propios y términos técnicos sin cambiar:",
  "subtitle_region": [530, 842, 1160, 1168],
  "ollama_url": "http://localhost:11434/api/generate",
  "ollama_model": "llama3.1:8b",
  "max_text_length": 500
}
```

### Parámetros de configuración

- `translation_prompt`: El contexto/instrucciones que se envían al modelo para la traducción
- `subtitle_region`: Coordenadas de la zona de subtítulos [izquierda, arriba, derecha, abajo]
- `ollama_url`: URL de la API local de Ollama
- `ollama_model`: Modelo de Ollama a usar para traducción
- `max_text_length`: Longitud máxima del texto a traducir

### Configuración rápida de coordenadas

Para encontrar las coordenadas exactas de tu zona de subtítulos:
1. Abre una reunión con subtítulos
2. Usa herramientas como Digital Color Meter (macOS) para encontrar las coordenadas
3. Ajusta los valores en `config.json`

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
