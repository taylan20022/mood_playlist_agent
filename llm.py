import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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

response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    return json.loads(response.choices[0].message.content)


