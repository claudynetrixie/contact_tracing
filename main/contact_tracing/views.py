# pip freeze > requirements.txt
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
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


def homepage(request):
    tic = time.perf_counter()

    # top 10 most populated
    num = 10
    labels = []
    data = []

    filter_r = RoomFilter(request.GET, queryset=Room.objects.all())
    filter_r.form.fields['building'].label = "Area"

    toc = time.perf_counter()
    print(f"Drop down loading in {toc - tic:0.4f} seconds")

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
    # print(labels)
    # print(data)
    # print(f"For loop in {toc - tic:0.4f} seconds")

    # labels =['F-23', 'F-15', 'D-40', 'A-3', 'C-36', 'A-37', 'A-22', 'D-13', 'F-27', 'B-22']
    # data =[639, 549, 545, 523, 523, 516, 502, 501, 496, 492]

    room_count = []
    room_number = 10
    # for room in range(1, room_number + 1):
    #     print(room)
    #     mydict = {"room_id": room,
    #               "date_start": "2020-08-09",
    #               "date_end": "2020-08-15",
    #               "time_start": "8:00",
    #               "time_end": "16:00"}
    #
    #     qstr = urlencode(mydict, doseq=True)
    #
    #     res = urllib.request.urlopen(urllib.request.Request(
    #          # url= "https://1cgw622rr4.execute-api.ap-southeast-1.amazonaws.com/test2/locationcount/?room_id=12&date_start=2020-08-09&date_end=2020-08-15&time_start=8:00&time_end=16:00",
    #         url = 'https://1cgw622rr4.execute-api.ap-southeast-1.amazonaws.com/test2/locationcount/?' + qstr,
    #         headers={'Accept': 'application/json', 'Connection': 'keep-alive'},
    #         method='GET'),
    #         timeout=5)
    #     # print(res.status)
    #     # print(res.reason)
    #     # print(json.loads(res.read()))
    #     response = json.loads(res.read())
    #     p = {'room': room, 'count': response['count']}
    #     room_count.append(p)

    mydict = {"room_id": 1,
                "date_start": "2020-08-09",
                "date_end": "2020-08-15",
                "time_start": "8:00",
                "time_end": "16:00"}

    qstr = urlencode(mydict, doseq=True)
    res = urllib.request.urlopen(urllib.request.Request(
           # url= "https://1cgw622rr4.execute-api.ap-southeast-1.amazonaws.com/test2/locationcount/?room_id=12&date_start=2020-08-09&date_end=2020-08-15&time_start=8:00&time_end=16:00",
          url = 'https://1cgw622rr4.execute-api.ap-southeast-1.amazonaws.com/test2/locationcount/?' + qstr,
          headers={'Accept': 'application/json', 'Connection': 'keep-alive'},
          method='GET'),
          timeout=5)
      # print(res.status)
      # print(res.reason)
      # print(json.loads(res.read()))
    response = json.loads(res.read())
    #print(response)

    room_count_s = sorted(response, key=itemgetter('count'), reverse=True)[0:num]
    # room_count_s = response[0:num]
    for entry in room_count_s:
        labels.append(entry['room'])
        data.append(entry['count'])

    print(data)

    toc = time.perf_counter()
    print(f"End of for loop in {toc - tic:0.4f} seconds")

    # room_count_s = sorted(room_count, key=itemgetter('count'), reverse=True)[0:num]

    toc = time.perf_counter()
    print(f"Sorted in {toc - tic:0.4f} seconds")

    # for entry in room_count_s:
    #     labels.append(entry['room'])
    #     data.append(entry['count'])

    toc = time.perf_counter()
    print(f"Chart loading data in {toc - tic:0.4f} seconds")

    return render(request=request,
                  context={
                      'labels': labels,
                      'data': data,
                      'filter_r': filter_r,
                      # 'date_bf': date_bf,
                      # 'date_af': date_af,
                      # 'time_bf': time_bf,
                      # 'time_af': time_af,
                  },
                  template_name='templates/main/home.html')

# def bar_graph(request):
    

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

    myFilter = StatFilter(request.GET, queryset=stats)
    stat_f = myFilter.qs
    # .order_by('date', 'time')
    # buildings = Building.objects.all()

    if (request.GET):
        print("HELLO WORLD")
        payload = request.GET
        if (request.GET['date_before'] and request.GET['date_after'] and request.GET['time_before'] and request.GET[
            'time_after']):
            date_bf = payload['date_before']
            date_af = payload['date_after']
            time_bf = "{0}:00".format(payload['time_before'].split(":")[0])
            stat_f = stat_f.filter(date__range=[payload['date_before'], payload['date_after']],
                                   time__range=[time_bf, payload['time_after']])
            time_bf = payload['time_before']
            time_af = payload['time_after']
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
