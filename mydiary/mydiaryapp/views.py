from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import DiaryNoteSerializer
from .models import DiaryNote
from django.http import Http404


# Create your views here.

class MyHellAPIView(APIView):
    def get(self, request, format=None):
        respStr = [

            'Тестовый сервис 1',
            'Нагрузочный сервис 2'

        ]
        return Response({'message': ' API tutvintage.ru', 'respString': respStr})


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
