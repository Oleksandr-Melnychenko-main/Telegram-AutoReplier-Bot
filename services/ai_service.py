from pathlib import Path
from os import getenv
import logging
from openai import OpenAI


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


api_key = getenv("AI_API_TOKEN")
client = OpenAI(api_key=api_key)


def generate_ai_response(user_message: str) -> str:
    if not user_message:
        user_message = "Чо малчім?"

    try:
        response = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {"role": "system", "content": MY_PERSONA_PROMPT},
            ],
            temperature=0.7
        )

        ai_text = response.choices[0].message.content

        if not ai_text: 
            return "Атебісь ат мєня, я вже заєбався відповідати"
        
        return ai_text
        
    except Exception as e:
        error_msg = str(e)

        if "503" in error_msg or "UNAVAILABLE" in error_msg:
            return "Оскільки є мільйони інших дибілів, які юзають APIшку ШІшки для всякої хуйні, у гугла перегрілися серваки, тому запхайте свої питання собі поглибше"
            
        elif "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg or "Rate limit" in error_msg:
            return "Дєвачкі, я нє рєзінавий, ліміт питань так то існує, тому або ждіть або йдіть наху"
        
        logging.error(f"OpenAI API Error: {e}")
        return "Атебісь ат мєня, я вже заєбався відповідати"
    