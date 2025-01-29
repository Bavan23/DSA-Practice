import requests

API_KEY = "AIzaSyBc5qm8E0JHCWf08VJ1x4c3rmDIC_w3Uno"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

data = {
    "contents": [{"parts": [{"text": "Explain how AI works"}]}]
}

headers = {"Content-Type": "application/json"}

response = requests.post(URL, json=data, headers=headers)
print(response.json())  # Print API response
import requests

API_KEY = "YOUR_GEMINI_API_KEY"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

data = {
    "contents": [{"parts": [{"text": "Explain how AI works"}]}]
}

headers = {"Content-Type": "application/json"}

response = requests.post(URL, json=data, headers=headers)
print(response.json())  # Print API response

