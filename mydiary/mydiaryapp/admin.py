from django.contrib import admin
from .models import Patient, Resource, ScheduleRecord


# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ('fullName', 'policy')
    list_display_links = ('fullName', 'policy')
    search_fields = ('fullName', 'policy')

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('resourceId','doctorName', 'specialityName', 'cabNum', 'duration')
    list_filter = ('doctorName', 'specialityName')
    list_display_links = ('doctorName', 'specialityName')
    search_fields = ('doctorName', 'specialityName')

class RecordAdmin(admin.ModelAdmin):
    list_display = ('resourceId', 'patientId', 'recordDate')
    list_filter = ('resourceId', 'patientId', 'recordDate')
    list_display_links =  ('resourceId', 'patientId','recordDate')
    search_fields = ('resourceId', 'patientId')

admin.site.register(Patient, PatientAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(ScheduleRecord, RecordAdmin)