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

class Patient(models.Model):
    patientId = models.IntegerField()
    fullName = models.CharField(max_length=200)
    birthDate = models.CharField(max_length=10)
    policy = models.CharField(max_length=30)
    lpuId = models.IntegerField()


    def __str__(self):
        return self.fullName

class Resource(models.Model):
    resourceId = models.IntegerField()
    doctorId = models.IntegerField()
    doctorName = models.CharField(max_length=255)
    specialityId = models.IntegerField()
    specialityName = models.CharField(max_length=255)
    duration = models.IntegerField()
    cabNum = models.CharField(max_length=25)
    timeAvail = models.CharField(max_length=255)
    timeUnavail = models.CharField(max_length=255)
    maskAvail = models.CharField(max_length=20)
    maskUnavail = models.CharField(max_length=20)
    comment = models.CharField(max_length=50)

    def __str__(self):
        return self.doctorName + ' ' + self.specialityName  + ' каб.' + self.cabNum


class ScheduleRecord(models.Model):
    patientId = models.ForeignKey(Patient, on_delete=models.CASCADE)
    resourceId = models.ForeignKey(Resource, on_delete=models.CASCADE)
    recordTime = models.CharField(max_length=5)
    recordTimeTo = models.CharField(max_length=5, null=True)
    recordDate = models.DateTimeField()

    def srecord_get(self):
        return self.recordDate, self.patientId

