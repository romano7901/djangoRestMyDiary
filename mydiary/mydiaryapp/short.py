import pandas as pd
import datetime
import json


maxDaysShedule = 60
shedule_all = []
shedule_resource = []

# Generate quotes for all days by week masks and time intervals
def generateRecourceQuote(maxDaysShedule, maskWP, maskWN, duration,timeAvail, timeUnavail, comment):
    dateAvail = []
    dateUnavail = []

    startDate = datetime.datetime.now()
    toDate = startDate + datetime.timedelta(days=maxDaysShedule)
    # generate appointment dates  2021-10-07T10:00:00+03:00
    dateAvail = pd.bdate_range(startDate, toDate, freq='C', weekmask=maskWP, holidays=None)\
        .strftime("%Y-%m-%dT%H:%M:%S+03:00").tolist()
    dateUnavail = pd.bdate_range(startDate, toDate, freq='C', weekmask=maskWN, holidays=None)\
        .strftime("%Y-%m-%dT%H:%M:%S+03:00").tolist()


    for da in dateAvail:

        time_quotes = []
        # print(da)
        for i in timeAvail:
            genDayQuote(da+' '+i[0][0],da+' '+ i[1][0], duration, True, '', time_quotes)
        if da in dateUnavail:
            for j in timeUnavail: genDayQuote(da+' '+j[0][0],da+' '+ j[1][0], 0, False, comment, time_quotes)
        #print(time_quotes)
        shedule_resource_date = {
            'sheduleDate': da
        }
        shedule_resource.append(da)

# Generate  time intervals
def genDayQuote(timeStart, timeEnd, duration, avail, comment , time_quotes):
    time_slot = {}
    if avail:

        time_slot = {'timeFrom': timeStart, 'timeTo':timeEnd, 'apointment': avail,'quoteStatus': 'Принимает',
                     'patients': []}
        time_quotes.append(time_slot)

    else:
        time_slot = {'timeFrom': timeStart, 'timeTo':timeEnd, 'apointment': avail,'quoteStatus': comment,
                     'patients': []}
        time_quotes.append(time_slot)

#   Григорьева Г.Г.Терапевт
maskWP = '1111100'
maskWN = '1111100'
timeAvail = [(['10:00'], ['14:00']), (['15:00'], ['20:00'])]
timeUnavail = [(['14:00'], ['15:00'])]
comment = 'Врач не работает'
duration = 30
shedule_resource = []
generateRecourceQuote(maxDaysShedule, maskWP, maskWN, duration, timeAvail, timeUnavail, comment)
shedule_resource_main = {
    'resourceId': 1234567,
    'doctorId': 667660,
    'doctorName': 'Григорьева Г.Г.',
    'specialityId': 54321,
    'specialityName': 'Терапевт',

    'sheduleList': shedule_resource}
shedule_all.append(shedule_resource_main)

#  Сидорова С.С.Терапевт
maskWP = '1111000'
maskWN = '1000000'
timeAvail = [(['10:00'], ['15:00'])]
timeUnavail = [(['10:00'], ['15:00'])]
comment = 'Обучение'
duration = 30
shedule_resource = []
generateRecourceQuote(maxDaysShedule, maskWP, maskWN, duration, timeAvail, timeUnavail, comment)
shedule_resource_main = {
    'resourceId': 123444567,
    'doctorId': 99955666,
    'doctorName': 'Сидорова С.С.',
    'specialityId': 54321,
    'specialityName': 'Терапевт',

    'sheduleList': shedule_resource}
shedule_all.append(shedule_resource_main)

#  Сидорова С.С.Терапевт
maskWP = '0000110'
maskWN = '0000001'
timeAvail = [(['14:00'], ['18:00'])]
timeUnavail = [([], [])]
comment = ''
duration = 10
shedule_resource = []
generateRecourceQuote(maxDaysShedule, maskWP, maskWN, duration, timeAvail, timeUnavail, comment)
shedule_resource_main = {
    'resourceId': 1234995567,
    'doctorId': 99955666,
    'doctorName': 'Сидорова С.С.',
    'specialityId': 54321,
    'specialityName': 'Терапевт',

    'sheduleList': shedule_resource}
shedule_all.append(shedule_resource_main)

#   Елисеева Е.Е. Офтальмолог
maskWP = '1111100'
maskWN = '1111100'
timeAvail = [(['14:00'], ['18:00'])]
timeUnavail = [(['14:30'], ['14:55']),(['16:20'], ['16:40'])]
comment = 'Работа с документами'
duration = 30
shedule_resource = []
generateRecourceQuote(maxDaysShedule, maskWP, maskWN, duration,timeAvail, timeUnavail, comment)
shedule_resource_main = {
    'resourceId': 55544555567,
    'doctorId': 66545355660,
    'doctorName': 'Елисеева Е.Е.',
    'specialityId': 55667788,
    'specialityName': 'Офтальмолог',

    'sheduleList': shedule_resource}

shedule_all.append(shedule_resource_main)

#   Константинова-Щедрина А.А.Офтальмолог
maskWP = '0111110'
maskWN = '0100000'
timeAvail = [(['09:00'], ['21:00'])]
timeUnavail = [(['09:00'], ['12:00'])]
comment = 'Не принимает'
duration = 30
shedule_resource = []
generateRecourceQuote(maxDaysShedule, maskWP, maskWN, duration,timeAvail, timeUnavail, comment)
shedule_resource_main = {
    'resourceId': 5554567,
    'doctorId': 6655660,
    'doctorName': 'Константинова-Щедрина А.А.',
    'specialityId': 55667788,
    'specialityName': 'Офтальмолог',

    'sheduleList': shedule_resource}

shedule_all.append(shedule_resource_main)

json_data = json.dumps(shedule_all, ensure_ascii=False)

