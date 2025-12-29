import json
import streamlit as st
from openai import OpenAI

ALLOWED_MOODS = ["sad", "happy", "energetic", "calm"]

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def analyze_user_input(user_input: str):
    prompt = f"""
You are an intent parser.

Allowed moods: {ALLOWED_MOODS}

User input: "{user_input}"

Return ONLY valid JSON in this format:
{{
  "mood": "sad | happy | energetic | calm",
  "artist": "optional artist name or null"
}}
"""

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )

        raw_text = response.output_text.strip()
        return json.loads(raw_text)

    except Exception as e:
        # This will show the REAL OpenAI error in Streamlit
        st.error(f"OpenAI API error: {e}")
        return {
            "mood": "calm",
            "artist": None
        }
