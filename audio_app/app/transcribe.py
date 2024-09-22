import os

# Load the Whisper model


def transcribe_audio(audio_data):
    path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "myfile.mp3"
    )
    if os.path.exists(path):
        os.remove(path)
    with open(path, mode="bx") as f:
        f.write(audio_data)
    import requests

    # Define your OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")

    # Define the API endpoint
    url = "https://api.openai.com/v1/audio/transcriptions"

    # Open the audio file in binary mode
    audio_file = open(path, "rb")

    # Set up the headers with the API key
    headers = {"Authorization": f"Bearer {api_key}"}

    # Set up the data to specify the model you want to use (e.g., "whisper-1")
    data = {"model": "whisper-1"}

    # Make the POST request to the transcription endpoint
    response = requests.post(
        url, headers=headers, data=data, files={"file": audio_file}
    )

    # Close the audio file after sending the request
    audio_file.close()

    # Check if the request was successful
    if response.status_code == 200:
        transcription = response.json()
        print(transcription["text"])  # Print the transcribed text
        return transcription["text"]
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return "Error: Unable to transcribe audio"
