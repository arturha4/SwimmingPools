from django.db import models

from main.models.timetable_slot import TimetableSlot


class Track(models.Model):
    timetable_slots = models.ForeignKey(TimetableSlot, models.DO_NOTHING)
