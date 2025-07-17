# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python script that performs real-time OCR (Optical Character Recognition) and translation of subtitles from screen captures. It's designed specifically for macOS to capture subtitle regions during video calls (Teams, Google Meet, etc.) and translate them from English to Spanish using a local Ollama model.

## Architecture

The project consists of a single main script (`ocr_translate.py`) that:
1. Captures screenshots of a defined screen region containing subtitles
2. Extracts text using Tesseract OCR via pytesseract
3. Sends the text to a local Ollama API for translation
4. Displays results in the terminal

Key components:
- **Screen capture**: Uses PIL's ImageGrab to capture specific screen coordinates
- **OCR processing**: Uses pytesseract wrapper for Tesseract OCR engine
- **Translation**: Makes HTTP requests to local Ollama API (default: llama3.1:8b model)
- **Main loop**: Continuously monitors for new subtitle text every second

## Dependencies

The project uses Python 3.8+ with these dependencies (defined in `requirements.txt`):
- `pillow` - For image processing and screen capture
- `pytesseract` - Python wrapper for Tesseract OCR
- `requests` - For HTTP requests to Ollama API

## System Requirements

- macOS (uses macOS-specific screen capture)
- Tesseract OCR installed via Homebrew (`brew install tesseract`)
- Ollama running locally with a model (default: llama3.1:8b)

## Common Commands

### Setup
```bash
# Install Python dependencies
pip3 install -r requirements.txt

# Install Tesseract OCR (one-time setup)
brew install tesseract
```

### Running the Application
```bash
# Start the OCR and translation process
python3 ocr_translate.py
```

### Configuration
Before running, adjust the subtitle region coordinates in `ocr_translate.py`:
```python
SUBTITLE_REGION = (530, 842, 1160, 1168)  # (left, top, right, bottom)
```

## Key Configuration Variables

- `SUBTITLE_REGION`: Screen coordinates for subtitle capture area
- `OLLAMA_URL`: Local Ollama API endpoint (default: http://localhost:11434/api/generate)
- `OLLAMA_MODEL`: Ollama model to use for translation (default: llama3.1:8b)

## Important Notes

- The script is designed for local processing only - no external services are used
- Text is limited to 500 characters to prevent overloading the translation model
- The main loop runs every second to avoid CPU overload
- All processing happens locally for privacy