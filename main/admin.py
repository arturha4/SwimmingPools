from django.contrib import admin
from main.models.timetable_slot import TimetableSlot
from main.models.track import Track

admin.site.register(TimetableSlot)
admin.site.register(Track)