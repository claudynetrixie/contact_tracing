from django.db import models
from datetime import datetime


class Building(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Room(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Log(models.Model):
    time_created = models.DateTimeField()


class Stat(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    count = models.IntegerField()
    count_unique = models.IntegerField()

    def date_time(self):
        return '%s %s' % (self.date, self.time)

    def time_range(self):
        t2 = int(self.time.hour) + 1
        if t2 == 24:
            t2 = 0
        time2 = "%s:00:00" % (str(t2))
        return '%s - %s' % (self.time, time2)


class InfectionReport(models.Model):
    date_tested = models.DateField()
    time_recorded = models.DateTimeField()


class LocationLog(models.Model):
    infection_report = models.ForeignKey(InfectionReport, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    e_time = models.IntegerField()
    duration = models.FloatField()


class Parameter(models.Model):
    loc_count = models.IntegerField()

    
class PeakData(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    time = models.TimeField()
    rank = models.IntegerField()


class PeakHour(models.Model):
    time = models.TimeField()
    count = models.IntegerField()


class PopData(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    count = models.IntegerField()
    rank = models.IntegerField()


class User(models.Model):
    key = models.BinaryField()
    name = models.CharField(max_length=50)

class Server(models.Model):
    public_key = models.BinaryField()
    private_key = models.BinaryField()




