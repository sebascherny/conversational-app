import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .transcribe import transcribe_audio
from .chat import get_gpt_response
from .tts import text_to_speech


class AudioConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        if bytes_data:
            # Convert audio to text using Whisper
            transcript = transcribe_audio(bytes_data)
            print("TRANSCIRPT", transcript)

            # Send text to GPT-3.5 and get response
            gpt_response = get_gpt_response(transcript)
            print("GPT RESPONSE", gpt_response)

            # Convert GPT-3.5 response to audio using gTTS
            response_audio = text_to_speech(gpt_response)

            # Send the audio response back to the client
            await self.send(bytes_data=response_audio)

    async def disconnect(self, close_code):
        pass
