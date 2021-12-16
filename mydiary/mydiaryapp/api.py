from .models import DiaryNote, Message
from .serializer import DiaryNoteSerializer, MessageSerializer
from rest_framework import viewsets, permissions


class DiaryNoteViewSet(viewsets.ModelViewSet):
    queryset = DiaryNote.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DiaryNoteSerializer




class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MessageSerializer
