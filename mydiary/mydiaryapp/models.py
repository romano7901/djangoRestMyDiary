from django.db import models


# Create your models here.

class DiaryNote(models.Model):
    title = models.CharField(max_length=90)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# refer to amazon s3 storage keys
class DiaryImage(models.Model):
    s3key = models.CharField(max_length=255, blank=False)
    s3url = models.CharField(max_length=255, blank=True)
    diarynote = models.ForeignKey(DiaryNote, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return self.s3key


# one conversation
class Conversation(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    creator = models.IntegerField(default=12345)
    isDeleted = models.BooleanField(default=False)


# messages from one conversation
class Message(models.Model):
    userId = models.IntegerField(default=54321)
    text = models.CharField(max_length=500)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
