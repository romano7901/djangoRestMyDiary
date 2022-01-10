import pandas as pd
from datetime import datetime
from datetime import timedelta
from .models import Resource, ScheduleRecord, Patient
from django.db.models import Q
import json




# Generate  time intervals
def gen_day_quote(timeStart, timeEnd, avail, comment, time_quotes, patients_list):
    if avail:
        comment = 'Принимает'
    else:
        patients_list = []
    time_slot = {'timeFrom': timeStart, 'timeTo': timeEnd, 'apointment': avail, 'quoteStatus': comment,
                 'patients': patients_list}
    time_quotes.append(time_slot)


# Generate quotes for all days by week masks and time intervals
def gen_resource_quote(shedule_resource, start, resourceId, r_id , max_days, maskWP, maskWN, timeA, timeU):
    dateAvail = []
    dateUnavail = []


    timeAvail = json.loads(timeA)
    timeUnavail = json.loads(timeU)

    startDate = datetime.strptime(start, '%d.%m.%Y')
    toDate = startDate + timedelta(days=max_days)

    # generate appointment dates
    dateAvail = pd.bdate_range(startDate, toDate, freq='C', weekmask=maskWP, holidays=None) \
        .strftime("%Y-%m-%d").tolist()
    dateUnavail = pd.bdate_range(startDate, toDate, freq='C', weekmask=maskWN, holidays=None) \
        .strftime("%Y-%m-%d").tolist()

    # get all records for resourceId

    for da in dateAvail:
        da_ = datetime.strptime(da, '%Y-%m-%d').date()
        # check if has patient on this date and resourceId then add section patients resourceId=r_id
        patients = ScheduleRecord.objects.filter(Q(recordDate__date=da_)&Q(resourceId=r_id))
        patients_list = []
        for k in patients:
           time_from = da + 'T' + k.recordTime + ':00+03:00'
           time_to = da + 'T' + k.recordTimeTo + ':00+03:00'
           patient = Patient.objects.get(id=k.patientId_id)
           one_record = {
               'patientId': patient.patientId,
               'timeFrom': time_from,
               'timeTo': time_to,
           }
           patients_list.append(one_record)
        #print(patients_list)
        time_quotes = []


        for i in timeAvail:
           gen_day_quote(da + 'T' + i[0] + ':00+03:00', da + 'T' + i[1] + ':00+03:00', True, '', time_quotes, patients_list)
           if da in dateUnavail:
             for j in timeUnavail:
                gen_day_quote(da + 'T' + j[0] + ':00+03:00', da + 'T' + j[1] + ':00+03:00', False, j[2], time_quotes, patients_list)

        shedule_resource_date = {
            'resourceId': resourceId,
            'timeQuotes': time_quotes
        }
        shedule_resource.append(shedule_resource_date)


def generateScheduleJson(max_days, start, resources):

    shedule_resource = []
    res_list = resources.split(',')
    for i in res_list:
        resource = Resource.objects.get(resourceId=i)
        gen_resource_quote(shedule_resource,
                           start,
                           resource.resourceId,
                           resource.id,
                           max_days-1,
                           resource.maskAvail, resource.maskUnavail,
                           resource.timeAvail, resource.timeUnavail)

    return shedule_resource
