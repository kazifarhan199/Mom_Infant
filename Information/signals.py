import os
import csv
import datetime
from django.conf import settings

def postSaveRawDataSignal(sender, instance, created, **kwargs):
    print("Processing data....")
    data = instance.get_json()

    if type(data) == list:
        data = {"data": data}

    for key in data.keys():
        if not data.get(key):
            continue

        values = data.get(key)
        for value in values:
            if not value.get('startTimeInSeconds'):
                continue

            stamp = datetime.datetime.utcfromtimestamp(value['startTimeInSeconds'])
            
            if value.get('timeOffsetHeartRateSamples'):
                head = 'timeOffsetHeartRateSamples'
            elif value.get('timeOffsetBodyBatteryValues'):
                head = 'timeOffsetBodyBatteryValues'
            elif value.get('timeOffsetStressLevelValues'):
                head = 'timeOffsetStressLevelValues'
            elif value.get('startTimeOffsetInSeconds'):
                if value.get('timeOffsetEpochToBreaths'):
                    head = 'timeOffsetEpochToBreaths'
                elif value.get('hrvValues'):
                    head = 'hrvValues'
                elif value.get('timeOffsetSleepSpo2'):
                    head = 'timeOffsetSleepSpo2'
                elif value.get('timeOffsetSpo2Values'):
                    head = 'timeOffsetSpo2Values'
                else:
                    continue
            else:
                continue

            clean_data = value[head]

            if value.get('userAccessToken') == '2f8237b1-7033-4128-9842-bc8c2b94b396':
                color = 'white'
            elif value.get('userAccessToken') == '9bb9ee80-6e98-41d6-9d77-4e095a6e3064':
                color = 'blue'
            elif value.get('userAccessToken') == 'aeaa2d82-8fec-4bf2-a202-cff34734ddbf':
                color = 'red'
            else:
                color = "Dont_know_who"

            

            file_name = f"{color}-{key}-{head}-{stamp.date()}-{stamp.time().hour}:{stamp.time().minute}.csv"
            
            data_file = open("data/"+file_name, 'w')
            csv_writer = csv.writer(data_file)
            header = ['time', head]

            csv_writer.writerow(header)
            for c_data in clean_data.items():
                tim = stamp + datetime.timedelta(0, int(c_data[0]))
                csv_writer.writerow([tim, c_data[1]])
            data_file.close()
            
            os.system(f'cd data && curl -1 -v --disable-epsv --ftp-skip-pasv-ip -u {settings.BOX_EMAIL}:{settings.BOX_PASSWORD} --ftp-ssl --upload-file "{file_name}" ftp://ftp.box.com/Watch_Vitals/ &')
