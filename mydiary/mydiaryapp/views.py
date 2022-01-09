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
        respStr = {
            'Admin page':'http://52.14.250.218:8000/admin',
            'Patient search':'http://52.14.250.218:8000/patients/',
            'Resource list and search':'http://52.14.250.218:8000/resources/',
            'Schedule for resource': 'http://52.14.250.218:8000/schedule/09.01.2022/0/1111,2222,3333,4444,6666,7777,8888,5555/'

        }

        return Response(respStr)


class MyDiaryNoteList(APIView):
    noteSet = DiaryNote.objects.all()
    serial = DiaryNoteSerializer(noteSet, many=True)

    def get(self, request, format=None):
        return Response(self.serial.data)


class PatientList(APIView):


    def get(self, request, format=None):
        search = request.query_params.get('search')
        patientSet = []
        if search is not None:
            patientSet = Patient.objects.filter(Q(fullName__icontains=search) | Q(policy__icontains=search)).order_by('fullName')[:40]
        serial = PatientSerializer(patientSet, many=True)
        return Response(serial.data)


class ResourceList(APIView):
    resourceSet = Resource.objects.all()
    def get(self, request, format=None):
        search = request.query_params.get('search')
        if search is not None:
            self.resourceSet = self.resourceSet.filter(Q(specialityName__icontains=search) | Q(doctorName__icontains=search))
        serial = ResourceSerializer(self.resourceSet, many=True)
        return Response(serial.data)



class ScheduleAPIView(APIView):
     def get(self, request, start, days, resources, format=None):
        resp_str = generateScheduleJson(days, start, resources)
        return Response(resp_str)