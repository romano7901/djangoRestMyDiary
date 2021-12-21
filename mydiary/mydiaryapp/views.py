from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import DiaryNoteSerializer
from .models import DiaryNote
from django.http import Http404
from .short import *


# Create your views here.

class MyHellAPIView(APIView):
    def get(self, request, format=None):
        respStr = generateScheduleJson(3)
        return Response(respStr)


class MyDiaryNoteList(APIView):
    noteSet = DiaryNote.objects.all()
    serial = DiaryNoteSerializer(noteSet, many=True)

    def get(self, request, format=None):
        return Response(self.serial.data)


class MyDiaryNoteDetail(APIView):
    def get_object(self, pk):
        try:
            return DiaryNote.objects.get(pk=pk)
        except DiaryNote.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        mynote = self.get_object(pk)
        serial = DiaryNoteSerializer(mynote)
        return Response(serial.data)

class ScheduleAPIView(APIView):
     def get(self, request, start, days, resources, format=None):
        respStr = generateScheduleJson(days, start, resources)
        return Response(respStr)