from rest_framework import serializers
from .models import DiaryNote, DiaryImage, Conversation, Message


class DiaryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryImage
        fields = ['s3key', 's3url']


class DiaryNoteSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True)

    class Meta:
        model = DiaryNote
        fields = ['id', 'title', 'desc', 'date','images']


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
