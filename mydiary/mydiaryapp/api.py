from .models import DiaryNote, Message, Resource
from .serializer import DiaryNoteSerializer, MessageSerializer, ResourceSerializer
from rest_framework import viewsets, permissions, filters


class DiaryNoteViewSet(viewsets.ModelViewSet):
    queryset = DiaryNote.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DiaryNoteSerializer



class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MessageSerializer


