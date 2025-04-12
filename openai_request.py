from openai import OpenAI
import user_config
import requests
import json

# 🔑 OpenAI Client setup
client = OpenAI(api_key=user_config.openai_key)

# 🧠 Send request using OpenAI
def send_request_openai(query):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": query
            }
        ]
    )
    return completion.choices[0].message.content

# 🌟 Send request using Gemini (Google AI)
def send_request_gemini(query):
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
        f"?key={user_config.gemini_key}"
    )

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": query}
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return f"Error: {response.status_code} - {response.text}"
