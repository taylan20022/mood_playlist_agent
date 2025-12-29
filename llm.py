import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load .env locally (Streamlit Cloud will ignore this, which is fine)
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("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"))

ALLOWED_MOODS = ["sad", "happy", "energetic", "calm"]

def analyze_user_input(user_input: str):
    prompt = f"""
You are an intent parser.

Allowed moods: {ALLOWED_MOODS}

User request:
"{user_input}"

Return ONLY valid JSON in this format:
{{
  "moods": [],
  "n_songs": number
}}

Rules:
- Infer moods from meaning (e.g. dancing → energetic + happy)
- If number is not mentioned, use 10
- Only use allowed moods
"""

    # ✅ NEW OpenAI Responses API (correct)
    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    # ✅ Correct way to extract text
    text_output = response.output_text.strip()

    # ✅ Parse JSON safely
    return json.loads(text_output)

