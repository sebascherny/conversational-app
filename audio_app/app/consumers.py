from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .transcribe import transcribe_audio
from .chat import get_gpt_response
from .tts import text_to_speech
from .models import AudioResponse

@database_sync_to_async
def create_audio_response_object(transcript, gpt_response):
    return AudioResponse.objects.create(
        transcribed_text=transcript, gpt_response=gpt_response
    )


class AudioConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        if bytes_data:
            transcript = transcribe_audio(bytes_data)
            print("TRANSCIRPT:", transcript)
            gpt_response = get_gpt_response(transcript)
            print("GPT RESPONSE:", gpt_response)
            response_audio = text_to_speech(gpt_response)
            await create_audio_response_object(transcript, gpt_response)
            await self.send(bytes_data=response_audio)

    async def disconnect(self, close_code):
        pass
