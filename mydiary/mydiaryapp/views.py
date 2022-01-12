from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import filters
from .serializer import DiaryNoteSerializer, PatientSerializer, ResourceSerializer, ScheduleRecordSerializer
from .models import DiaryNote, Patient, Resource, ScheduleRecord
from django.http import Http404
from .short import *
from .dates import generateDatesJson
from django.db.models import Q


# Create your views here.


class MyHellAPIView(APIView):
    def get(self, request, format=None):
        respStr = {
            'Admin page': 'http://52.14.250.218:8000/admin',
            'Patient search': 'http://52.14.250.218:8000/patients/?search=але',
            'Patients by id': 'http://52.14.250.218:8000/patients/1,2,3,4,5/',
            'Available dates': 'http://52.14.250.218:8000/dates/1111,2222,3333,4444,6666,7777,8888,5555/',
            'Resource list and search': 'http://52.14.250.218:8000/resources/',
            'Schedule for resource': 'http://52.14.250.218:8000/schedule/17.01.2022/7/1111,2222,3333,4444,6666,7777,8888,5555/'

        }

        return Response(respStr)


class MyDiaryNoteList(APIView):
    noteSet = DiaryNote.objects.all()
    serial = DiaryNoteSerializer(noteSet, many=True)

    def get(self, request, format=None):
        return Response(self.serial.data)


class RecordAdd(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        return Response("ok")

    def post(self, request, format=None):
        patient = Patient.objects.get(patientId=request.data['patientId'])
        resource = Resource.objects.get(resourceId=request.data['resourceId'])
        record = ScheduleRecord(
            patientId=patient,
            resourceId=resource,
            recordTime=request.data['timeFrom'],
            recordTimeTo=request.data['timeTo'],
            recordDate=datetime.strptime(request.data['date'], '%d.%m.%Y')
        )
        record.save()
        return Response('Ok')


class PatientList(APIView):

    def get(self, request, format=None):
        search = request.query_params.get('search')
        patientSet = []
        if search is not None:
            patientSet = Patient.objects.filter(
                Q(fullName__istartswith=search) | Q(policy__istartswith=search)).order_by('fullName')[:40]
        for pt in patientSet:
            name = pt.fullName.split(' ')
            pt.shortName = f'{name[0]} {name[1][0]}.{name[2][0]}.'
        serial = PatientSerializer(patientSet, many=True)
        return Response(serial.data)


class PatientListById(APIView):

    def get(self, request, id, format=None):
        search = request.query_params.get('search')
        patientSet = []
        if id is not None:
            id_list = id.split(',')
            patientSet = Patient.objects.filter(patientId__in=id_list)
        for pt in patientSet:
            name = pt.fullName.split(' ')
            pt.shortName = f'{name[0]} {name[1][0]}.{name[2][0]}.'
        serial = PatientSerializer(patientSet, many=True)
        return Response(serial.data)


class ResourceList(APIView):
    resourceSet = Resource.objects.all()

    def get(self, request, format=None):
        search = request.query_params.get('search')
        if search is not None:
            self.resourceSet = self.resourceSet.filter(
                Q(specialityName__icontains=search) | Q(doctorName__icontains=search))
        serial = ResourceSerializer(self.resourceSet, many=True)
        return Response(serial.data)


class ScheduleAPIView(APIView):
    def get(self, request, start, days, resources, format=None):
        resp_str = generateScheduleJson(days, start, resources)
        return Response(resp_str)



class DatesAPIView(APIView):
    def get(self, request, resources, format=None):
        resp_str = generateDatesJson(resources)
        return Response(resp_str)