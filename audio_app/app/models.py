from django.db import models


class AudioResponse(models.Model):
    transcribed_text = models.TextField()
    gpt_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response {self.id} - {self.created_at}"
