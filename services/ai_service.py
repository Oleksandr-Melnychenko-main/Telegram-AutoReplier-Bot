from pathlib import Path
from os import getenv
import logging
from google import genai
from google.genai.types import GenerateContentConfig


BASE_DIR = Path(__file__).resolve().parent
PERSONA_FILE_PATH = BASE_DIR / "persona.txt"
def load_persona() -> str:
    try:
        with open(PERSONA_FILE_PATH, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception as e:
        logging.error(f"Coudn't download prompt file: {e}")
        return "You are a casual chat responder."
MY_PERSONA_PROMPT = load_persona()


api_key = getenv("GEMINI_API_TOKEN")
client = genai.Client(api_key=api_key)

def generate_ai_response(user_message: str) -> str:
    if not user_message:
        user_message = "Hello!"

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_message,
            config=GenerateContentConfig(
                system_instruction=MY_PERSONA_PROMPT,
                temperature=0.7
            )
        )

        if not response.text: 
            return "Атебісь ат мєня, я вже заєбався відповідати"
        
        return response.text
        
        
    except Exception as e:
        error_msg = str(e)

        if "503" in error_msg or "UNAVAILABLE" in error_msg:
            return "Оскільки є мільйони інших дибілів, які юзають APIшку ШІшки для всякої хуйні, у гугла перегрілися серваки, тому запхайте свої питання собі поглибше"
            
        elif "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
            return "Дєвачкі, я нє рєзінавий, ліміт питань так то існує, тому або ждіть або йдіть наху"
        
        logging.error(f"Gemini API Error: {e}")
        return "Атебісь ат мєня, я вже заєбався відповідати"
    