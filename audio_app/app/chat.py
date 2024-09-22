import openai
import requests
import os

def get_gpt_response(prompt):
    # Define your OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")

    # Define the API endpoint
    url = "https://api.openai.com/v1/chat/completions"

    # Set up the headers with the API key
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    # Set up the data (payload) to specify the model, prompt, and other options
    data = {
        "model": "gpt-3.5-turbo",
        "max_tokens": 150,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    }

    # Make the POST request to the completions endpoint
    response = requests.post(url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response and extract the completion text
        response_json = response.json()
        print(response_json)
        return response_json["choices"][0]["message"]["content"].strip()
    else:
        # Handle the error case
        print(f"Error: {response.status_code} - {response.text}")
        return None
