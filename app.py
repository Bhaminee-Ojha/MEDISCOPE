from flask import Flask, request, jsonify, render_template
import os
import json
import re

# Correct import for new gemini API
import google.generativeai as genai

app = Flask(__name__)

# Set your API key globally
genai.configure(api_key=os.environ.get("AIzaSyAhqDUB5TiErS2aleRIMbyZx1hHXwM1Ml4"))

# ------------------ ROUTES ------------------ #

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    symptoms = request.form.get("symptoms", "")
    if not symptoms:
        return jsonify({"analysis": {"error": "No symptoms provided"}})

    try:
        # Call Gemini LLM
        response = genai.generate_content(
            model="gemini-2.0-flash",
            prompt=f"Analyze these symptoms and return probable diseases, severity, infectious potential, and advice in JSON:\n{symptoms}"
        )

        raw_text = response.raw_text

        # Extract JSON from Gemini response
        match = re.search(r'\{.*\}', raw_text, re.DOTALL)
        if match:
            analysis = json.loads(match.group())
        else:
            analysis = {
                "probable_diseases": ["Unknown"],
                "severity": "mild",
                "infectious_potential": "low",
                "advice": "Consult a doctor"
            }

        return jsonify({"analysis": analysis})

    except Exception as e:
        return jsonify({"analysis": {"error": str(e)}})

# ------------------ MAIN ------------------ #
if __name__ == "__main__":
    app.run(debug=True)
