import google.generativeai as genai
import json
import re

from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Get the key from the environment
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ Gemini API key not found! Please set GEMINI_API_KEY in your .env file.")

# Configure Gemini
genai.configure(api_key=api_key)

def analyze_symptoms(symptoms):
    prompt = f"""
    You are an AI health assistant (not a doctor).
    The user reports these symptoms: {symptoms}.
    Respond ONLY in valid JSON like this:
    {{
      "probable_diseases": ["Disease1", "Disease2"],
      "severity": "mild/moderate/severe",
      "infectious_potential": "low/medium/high",
      "advice": "Short paragraph of safe, preventive guidance."
    }}
    """

    model = genai.GenerativeModel("gemini-2.0-flash")  # your working model

    try:
        response = model.generate_content(prompt)
        text = response.text.strip()

        # Remove markdown code fences if present
        text = re.sub(r"```json|```", "", text).strip()

        # Parse JSON
        try:
            data = json.loads(text)
            return data
        except json.JSONDecodeError:
            return {"raw_text": text}

    except Exception as e:
        return {"error": str(e)}

