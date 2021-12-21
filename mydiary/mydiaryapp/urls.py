from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', MyHellAPIView.as_view()),
    path('schedule/<str:start>/<int:days>/<str:resources>/', ScheduleAPIView.as_view()),
    path('mynotes/', MyDiaryNoteList.as_view()),
    path('mynotes/<int:pk>/', MyDiaryNoteDetail.as_view())
]


