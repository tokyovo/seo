from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ChatSession(BaseModel):
    session_id = models.CharField(max_length=255, unique=True)
    flow_id = models.CharField(max_length=255)

    def __str__(self):
        return f"Session {self.session_id} (Flow: {self.flow_id})"

class Message(BaseModel):
    MESSAGE_TYPE_CHOICES = [
        ('user', 'User'),
        ('bot', 'Bot'),
        ('history', 'History'),
    ]

    session = models.ForeignKey(ChatSession, related_name='messages', on_delete=models.CASCADE)
    message_type = models.CharField(max_length=7, choices=MESSAGE_TYPE_CHOICES)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_message_type_display()} - {self.content[:50]}"
