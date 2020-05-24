from django.db import models


class Message(models.Model):
    author = models.TextField()
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author

