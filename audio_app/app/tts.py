from gtts import gTTS
import io


def text_to_speech(text):
    tts = gTTS(text, lang="en")
    audio_data = io.BytesIO()
    tts.write_to_fp(audio_data)
    audio_data.seek(0)
    return audio_data.read()
