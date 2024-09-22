from gtts import gTTS
import io


def text_to_speech(text):
    # Convert text to speech using gTTS
    tts = gTTS(text, lang="en")

    # Save the audio to a BytesIO object
    audio_data = io.BytesIO()
    tts.write_to_fp(audio_data)

    # Reset the buffer's position to the beginning
    audio_data.seek(0)

    # Return the audio data as bytes
    return audio_data.read()
