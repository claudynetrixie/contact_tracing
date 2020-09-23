import csv
from datetime import timedelta, datetime
from contact_tracing.models import *
with open('dummy1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(line_count)
        if line_count !=0:
            duration = row[2]
            site = row[3]
            b = row[4]
            date_time = row[4].split()
            date_p = date_time[0].strip()
            time_p = date_time[1].strip()
            start_dt = datetime.strptime(row[4].strip(), '%d/%m/%Y %H:%M')
            sec_add = timedelta(seconds= float(duration))
            end_dt = start_dt + sec_add
            print(str(start_dt) + "-" + str(end_dt))
            if(end_dt.hour != start_dt.hour):
                diff_hour = end_dt.hour - start_dt.hour + 1
                for x in range(0, diff_hour):
                    c_hour = start_dt.hour + x
                    stat = Stat.objects.get(room_id = int(site)+1, date= start_dt.date(), time = "{0}:00:00".format(c_hour))
                    stat.count = stat.count + 1
                    stat.save()
            else:
                stat = Stat.objects.get(room_id = int(site)+1, date= start_dt.date(), time = "{0}:00:00".format(start_dt.hour))
                stat.count = stat.count + 1
                stat.save()
        line_count+=1

                        
