from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters
from .serializer import DiaryNoteSerializer, PatientSerializer, ResourceSerializer
from .models import DiaryNote, Patient, Resource
from django.http import Http404
from .short import *
from django.db.models import Q


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

class PatientList(APIView):
    patientSet = Patient.objects.all()

    def get(self, request, format=None):
        search = request.query_params.get('search')

        if search is not None:
            self.patientSet = self.patientSet.filter(Q(fullName__icontains=search) | Q(policy__icontains=search))
        serial = PatientSerializer(self.patientSet, many=True)
        return Response(serial.data)

class ResourceList(APIView):
    resourceSet = Resource.objects.all()
    def get(self, request, format=None):
        search = request.query_params.get('search')
        if search is not None:
            self.resourceSet = self.resourceSet.filter(Q(specialityName__icontains=search) | Q(doctorName__icontains=search))
        serial = ResourceSerializer(self.resourceSet, many=True)
        return Response(serial.data)




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