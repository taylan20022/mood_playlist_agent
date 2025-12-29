import os
import json
from openai import OpenAI

if "OPENAI_API_KEY" not in os.environ:
    raise RuntimeError("OPENAI_API_KEY missing")

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

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
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    return json.loads(response.choices[0].message.content)
