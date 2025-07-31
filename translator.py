import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

def translate_text(text, target_lang):
    url = "https://text-translator2.p.rapidapi.com/translate"

    payload = {
        "source_language": "auto",
        "target_language": target_lang,
        "text": text
    }

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),  # Loaded securely
        "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
    }

    try:
        response = requests.post(url, data=payload, headers=headers)
        response.raise_for_status()
        result = response.json()
        return result["data"]["translatedText"]
    except Exception as e:
        return f"Error during translation: {e}"
