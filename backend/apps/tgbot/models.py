from django.db import models

from apps.users.models import UserExtended


class ChatHistory(models.Model):
    user = models.ForeignKey(UserExtended, on_delete=models.CASCADE)
    request_text = models.TextField()
    response_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.created_at}"
