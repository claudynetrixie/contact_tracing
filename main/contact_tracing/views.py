# pip freeze > requirements.txt
# from celery.decorators import task
from django.shortcuts import render
from .models import *
from django.http import HttpResponse, JsonResponse
from operator import itemgetter

from .filters import StatFilter, RoomFilter
import time

import urllib.request
from urllib.request import urlretrieve
from urllib.parse import urlencode
import json

date_start = "2020-08-09"
date_end = "2020-08-15"

room_number = 300
num = 10

def homepage(request):
    tic = time.perf_counter()
    filter_r = RoomFilter(request.GET, queryset=Room.objects.all())
    filter_r.form.fields['building'].label = "Area"

    time_list = []
    room_list = []

    for x in range(1,6):
        data = PeakData.objects.filter(rank = x)[0]
        time_list.append(data.time)
        room_list.append(data.room)

    num = range(1,6)
    peaklist = zip(num, time_list, room_list)
    print(time_list)
    print(room_list)

    toc = time.perf_counter()
    print(f"Filter menu done in {toc - tic:0.4f} seconds")


    # if (request.GET):
    #     payload = request.GET
    #     if (request.GET['date_before'] and request.GET['date_after'] and request.GET['time_before'] and request.GET[
    #         'time_after']):
    #
    #         date_bf = payload['date_before']
    #         date_af = payload['date_after']
    #         time_bf = "{0}:00".format(payload['time_before'].split(":")[0])
    #
    #         if (request.GET['building']):
    #             print("results of date, time, building")
    #             print(request.GET['building'])
    #             building = request.GET['building']
    #             room_list = []
    #             for x in list(Room.objects.filter(building_id=building).values('id')):
    #                 room_list.append(x['id'])
    #             print(room_list)
    #             stat_f = Stat.objects.filter(date__range=[payload['date_before'], payload['date_after']],
    #                                          time__range=[time_bf, payload['time_after']],
    #                                          room_id__in=room_list)
    #
    #
    #         else:
    #             stat_f = Stat.objects.filter(date__range=[payload['date_before'], payload['date_after']],
    #                                          time__range=[time_bf, payload['time_after']])
    #
    #         time_bf = payload['time_before']
    #         time_af = payload['time_after']
    #     elif request.GET['date_before'] and request.GET['date_after']:
    #         print("results of date")
    #         date_bf = payload['date_before']
    #         date_af = payload['date_after']
    #
    #         if (request.GET['building']):
    #             print(request.GET['building'])
    #             building = request.GET['building']
    #             room_list = []
    #             for x in list(Room.objects.filter(building_id=building).values('id')):
    #                 room_list.append(x['id'])
    #
    #             stat_f = Stat.objects.filter(date__range=[payload['date_before'], payload['date_after']],
    #                                          room_id__in=room_list)
    #         else:
    #             stat_f = Stat.objects.filterfilter(date__range=[payload['date_before'], payload['date_after']])
    #
    #
    #         time_bf = ""
    #         time_af = ""
    #     elif request.GET['time_before'] and request.GET['time_after']:
    #         print("results of time")
    #         time_bf = "{0}:00".format(payload['time_before'].split(":")[0])
    #
    #         if (request.GET['building']):
    #             print(request.GET['building'])
    #             building = request.GET['building']
    #             room_list = []
    #             for x in list(Room.objects.filter(building_id=building).values('id')):
    #                 room_list.append(x['id'])
    #
    #             stat_f = Stat.objects.filter(
    #                 time__range=[time_bf, payload['time_after']],
    #                 room_id__in=room_list)
    #         else:
    #             stat_f = Stat.objects.filter(time__range=[time_bf, payload['time_after']])
    #
    #         time_bf = payload['time_before']
    #         time_af = payload['time_after']
    #         date_bf = ""
    #         date_af = ""
    #
    #
    # else:
    #     stat_f = Stat.objects.filter(date__range=[date_start, date_end], time__range = ["8:00", "18:00"])
    #     #
    #     # myFilter = StatFilter(request.GET, queryset=stat)
    #     # stat_f = myFilter.qs
    #
    #     date_bf = "2020-08-09"
    #     date_af = "2020-08-15"
    #     time_bf = "8:00:00"
    #     time_af = "18:00"
    #
    #     toc = time.perf_counter()
    #     print(f"Filtered in {toc - tic:0.4f} seconds")

    # room_count = []
    #
    # for room in range(1, room_number + 1):
    #     stat_list = stat_f.filter(room_id=room)
    #     cnt = 0
    #     for x in stat_list:
    #         cnt = cnt + x.count
    #     p = {'room': Room.objects.get(id=room).name, 'count': cnt}
    #     room_count.append(p)
    #
    # room_count_s = sorted(room_count, key=itemgetter('count'), reverse=True)[0:num]
    #
    # for entry in room_count_s:
    #     labels.append(entry['room'])
    #     data.append(entry['count'])
    #




    return render(request=request,
                  context={
                      'filter_r': filter_r,
                      'peaklist': peaklist,
                      # 'date_bf': date_bf,
                      # 'date_af': date_af,
                      # 'time_bf': time_bf,
                      # 'time_af': time_af,
                  },
                  template_name='templates/main/home.html')

def get_data(request):
    tic = time.perf_counter()

    # labels =['F-23', 'F-15', 'D-40', 'A-3', 'C-36', 'A-37', 'A-22', 'D-13', 'F-27', 'B-22']
    # data =[639, 549, 545, 523, 523, 516, 502, 501, 496, 492]
    data = []
    labels = []

    # mydict = {"room_id": 1,
    #             "date_start": "2020-08-09",
    #             "date_end": "2020-08-15",
    #             "time_start": "8:00",
    #             "time_end": "16:00"}
    #
    # qstr = urlencode(mydict, doseq=True)
    # res = urllib.request.urlopen(urllib.request.Request(
    #        # url= "https://1cgw622rr4.execute-api.ap-southeast-1.amazonaws.com/test2/locationcount/?room_id=12&date_start=2020-08-09&date_end=2020-08-15&time_start=8:00&time_end=16:00",
    #       url = 'https://1cgw622rr4.execute-api.ap-southeast-1.amazonaws.com/test2/locationcount/?' + qstr,
    #       headers={'Accept': 'application/json', 'Connection': 'keep-alive'},
    #       method='GET'),
    #       timeout=5)
    # response = json.loads(res.read())
    # toc = time.perf_counter()
    # print(f"HTTP get done in {toc - tic:0.4f} seconds")

    # room_count_s = sorted(response, key=itemgetter('count'), reverse=True)[0:num]
    # for entry in room_count_s:
    #     labels.append(entry['room'])
    #     data.append(entry['count'])
    #
    # toc = time.perf_counter()
    # print(f"Chart data done in {toc - tic:0.4f} seconds")

    logs = PopData.objects.all()

    for log in logs:
        data.append(log.count)
        labels.append(log.room.name)

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def get_line(request):
    print("GETLINE")
    labels =['7:00', '8:00', '9:00', '10:00', '11:00', '12:00','1:00', '2:00', '3:00', '4:00', '5:00', '6:00','7:00']
    # data =[0, 1, 2, 3, 4, 5, 6, 7,8, 9, 10, 11, 12]
    data = []

    hour_count = PeakHour.objects.all()
    for x in hour_count:
        data.append(x.count)

    print(data)

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def load_rooms(request):
    building_id = request.GET.get('building')
    # building_id = request.GET['building']
    # print("hello world")
    # print(building_id)
    rooms = Room.objects.filter(building_id=building_id)
    # print(rooms)
    return render(request, 'templates/main/room_dropdown_list_options.html', {'rooms': rooms})


def stat_search(request):
    tic = time.perf_counter()

    stats = Stat.objects.all().order_by('date', 'time')
    filter_r = RoomFilter(request.GET, queryset=Room.objects.all())
    filter_r.form.fields['building'].label = "Area"
    # stats = filter_r.qs

    myFilter = StatFilter(request.GET, queryset=stats)
    stat_f = myFilter.qs
    myFilter.form.fields['room'].label = "Site"
    # .order_by('date', 'time')
    # buildings = Building.objects.all()

    if (request.GET):
        print("HELLO WORLD")
        payload = request.GET

        if request.GET['building']:
            b_no = request.GET['building']
            print("find all rooms nums")
            room_list = list(Room.objects.filter(building_id = b_no).values('id'))
            room_list = [x['id'] for x in room_list ]
            print(room_list)

            stat_f = stat_f.filter(room_id__in=room_list)



        if (request.GET['date_before'] and request.GET['date_after'] and request.GET['time_before'] and request.GET[
            'time_after']):
            date_bf = payload['date_before']
            date_af = payload['date_after']
            time_bf = "{0}:00".format(payload['time_before'].split(":")[0])
            stat_f = stat_f.filter(date__range=[payload['date_before'], payload['date_after']],
                                   time__range=[time_bf, payload['time_after']])
            time_bf = payload['time_before']
            time_af = payload['time_after']
            # print(stat_f)

        elif request.GET['date_before'] and request.GET['date_after']:
            date_bf = payload['date_before']
            date_af = payload['date_after']
            stat_f = stat_f.filter(date__range=[payload['date_before'], payload['date_after']])

        elif request.GET['time_before'] and request.GET['time_after']:
            time_bf = "{0}:00".format(payload['time_before'].split(":")[0])
            stat_f = stat_f.filter(time__range=[time_bf, payload['time_after']])
            time_bf = payload['time_before']
            time_af = payload['time_after']



    else:
        stat_f = {}
        date_bf = "2020-08-09"
        date_af = "2020-08-15"
        time_bf = ""
        time_af = ""

    toc = time.perf_counter()
    print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")

    return render(request=request,
                  context={
                      'stats': stat_f,
                      'filter': myFilter,
                      'filter_r': filter_r,
                      # 'buildings': buildings,
                      'date_bf': date_bf,
                      'date_af': date_af,
                      'time_bf': time_bf,
                      'time_af': time_af

                  },
                  template_name='templates/main/stat_search.html')

# top 20 Peak traffic time and location
# date_start= "2020-08-09"
# date_end = "2020-08-15"
# num = 20
# room_number = 300
#
# stat_list = Stat.objects.filter(date__range=[date_start, date_end]).order_by('-count')
# stat_list = stat_list[0:num]
#
# print("Top 20 Peak Traffic Time and Location")
# for stat in stat_list:
#     print(stat.room.name + "   " + str(stat.count) + "  " + str(stat.date) + "-" + str(stat.time))
#
# print("Top 20 most populated locations weekly")
# room_count = []
#
# for room in range(1, room_number+1):
#     stat_list = Stat.objects.filter(date__range=[date_start, date_end], room_id =room)
#     cnt = 0
#     for x in stat_list:
#         cnt = cnt + x.count
#     p = {'room': room, 'count': cnt}
#     room_count.append(p)
#
# room_count_s = sorted(room_count, key=itemgetter('count'), reverse = True)[0:num]
