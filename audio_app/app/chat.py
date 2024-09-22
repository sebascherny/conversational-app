import openai
import requests
import os

def get_gpt_response(prompt):
    api_key = os.getenv("OPENAI_API_KEY")
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    data = {
        "model": "gpt-3.5-turbo",
        "max_tokens": 150,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant. Always answer in English simulating you are a human."},
            {"role": "user", "content": prompt},
        ],
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        response_json = response.json()
        return response_json["choices"][0]["message"]["content"].strip()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
