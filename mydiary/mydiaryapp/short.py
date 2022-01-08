import pandas as pd
from datetime import datetime
from datetime import timedelta
from .models import Resource
import json




# Generate  time intervals
def gen_day_quote(timeStart, timeEnd, avail, comment, time_quotes):
    if avail:
        comment = 'Принимает'
    time_slot = {'timeFrom': timeStart, 'timeTo': timeEnd, 'apointment': avail, 'quoteStatus': comment,
                 'patients': []}
    time_quotes.append(time_slot)


# Generate quotes for all days by week masks and time intervals
def gen_resource_quote(shedule_resource, start, resourceId, max_days, maskWP, maskWN, timeA, timeU):
    dateAvail = []
    dateUnavail = []
    print(timeA)
    print(timeU)
    timeAvail = json.loads(timeA)
    timeUnavail = json.loads(timeU)




    startDate = datetime.strptime(start, '%d.%m.%Y')
    toDate = startDate + timedelta(days=max_days)

    # generate appointment dates
    dateAvail = pd.bdate_range(startDate, toDate, freq='C', weekmask=maskWP, holidays=None) \
        .strftime("%Y-%m-%dT").tolist()
    dateUnavail = pd.bdate_range(startDate, toDate, freq='C', weekmask=maskWN, holidays=None) \
        .strftime("%Y-%m-%dT").tolist()

    for da in dateAvail:
        time_quotes = []
        # print(da)

        for i in timeAvail:
           gen_day_quote(da + '' + i[0] + ':00+03:00', da + '' + i[1] + ':00+03:00', True, '', time_quotes)
           if da in dateUnavail:
             for j in timeUnavail:
                gen_day_quote(da + '' + j[0] + ':00+03:00', da + j[1] + ':00+03:00', False, j[2], time_quotes)

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
        print(resource.resourceId)
        gen_resource_quote(shedule_resource,
                           start,
                           resource.resourceId,
                           max_days,
                           resource.maskAvail, resource.maskUnavail,
                           resource.timeAvail, resource.timeUnavail)

    return shedule_resource
