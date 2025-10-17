import google.generativeai as genai

# Configure your Gemini API key (from Google AI Studio)
genai.configure(api_key="AIzaSyAhqDUB5TiErS2aleRIMbyZx1hHXwM1Ml4")

# ✅ Use correct new model name (supported in v0.8+)
model = genai.GenerativeModel("gemini-1.5-flash-latest")

response = model.generate_content("Say Hello if you are working.")
print(response.text)
