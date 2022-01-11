import pandas as pd
from datetime import datetime
from datetime import timedelta
from .models import Resource



def arrayOp(s_array):
    r_str = '0000000'
    for s in  s_array:
        r_str = orOpStr(r_str,s)
    return r_str

def orOpStr(str_a,str_b):
    str_c = ''
    for i in range(7):
        if int(str_b[i]+str_a[i])>=1:
            str_c = str_c+'1'
        else:
            str_c = str_c + '0'
    return str_c

def generateDatesJson(resources):
    avail_dates = {}
    res_list = resources.split(',')
    mask_list = []
    for i in res_list:
        resource = Resource.objects.get(resourceId=i)
        mask_list.append(resource.maskAvail)
    mask_total = arrayOp(mask_list)
    startDate = datetime.now()
    toDate = startDate + timedelta(days=90)

    dateAvail = pd.bdate_range(startDate, toDate, freq='C', weekmask=mask_total, holidays=None) \
        .strftime("%Y-%m-%dT00:00:00+03:00").tolist()
    return dateAvail

