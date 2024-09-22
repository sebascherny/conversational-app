import os


def transcribe_audio(audio_data):
    path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "myfile.mp3"
    )
    if os.path.exists(path):
        os.remove(path)
    with open(path, mode="bx") as f:
        f.write(audio_data)
    import requests
    api_key = os.getenv("OPENAI_API_KEY")
    url = "https://api.openai.com/v1/audio/transcriptions"
    audio_file = open(path, "rb")
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {"model": "whisper-1"}
    response = requests.post(
        url, headers=headers, data=data, files={"file": audio_file}
    )
    audio_file.close()
    if response.status_code == 200:
        transcription = response.json()
        return transcription["text"]
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return "Error: Unable to transcribe audio"
