from django.db import models
from embed_video.fields import EmbedVideoField
class Video(models.Model):
    title = models.CharField(max_length=100)
    videos = models.FileField(upload_to='video/%y')
    def __str__(self):
        return self.title
    class meta:
        ordering = ['-added']

# Create your models here.
