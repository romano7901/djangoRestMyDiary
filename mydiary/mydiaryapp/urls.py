from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', MyHellAPIView.as_view()),
    path('schedule/<str:start>/<int:days>/<str:resources>/', ScheduleAPIView.as_view()),
    path('patients/<str:id>/', PatientListById.as_view()),
    path('patients/', PatientList.as_view()),
    path('resources/', ResourceList.as_view()),
    path('record/', RecordAdd.as_view()),
    path('dates/<str:resources>/',DatesAPIView.as_view()),
  ]


