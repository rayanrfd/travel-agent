from openai import OpenAI, APIStatusError
import os
from dotenv import load_dotenv
from schemas.schemas import TravelPlan

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("💡 `OPENAI_API_KEY` non défini dans le fichier .env")

client = OpenAI(
    api_key=OPENAI_API_KEY,
    max_retries=0  # pour expliquer explicitement ; par défaut, 409/408/429 sont automatiquement rejoués deux fois :contentReference[oaicite:1]{index=1}
)

def get_response(prompt: str) -> TravelPlan | None:
    try:
        resp = client.responses.parse(
            model="gpt-4o-mini",
            input=[
                {"role": "system", "content": "You are a travel planner AI. Extract travel plans from user prompts."},
                {"role": "user", "content": prompt}
            ],
            text_format=TravelPlan,
        )
        return resp
    except APIStatusError as exc:
        print("status_code:", exc.status_code)
        try:
            err = exc.response.json()
            print("error body:", err)
        except Exception:
            print("raw body:", exc.response.text)
        print("request_id:", exc.request_id)
        # Exemple concret : "OpenAI-Organization header should match organization for API key" signifie que
        # la clé API n’est pas liée à l’org passée dans le header — il faut laisser traîner sur l’org par défaut :contentReference[oaicite:2]{index=2}
        raise
    except Exception as exc:
        print("Unexpected exception:", repr(exc))
        raise

def main():
    plan = get_response("I want to travel from Tokyo to Kyoto from 2023-10-01 to 2023-10-05.")
    if plan:
        print("TravelPlan:", plan)

if __name__ == "__main__":
    main()
