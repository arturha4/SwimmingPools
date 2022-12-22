from django.urls import re_path, include

from main.controllers.timetable import Timetable
from main.controllers.timetable_slot import TimetableSlot
from main.controllers.track_seed import TrackSeed

urlpatterns = [
    re_path(r'^timetable/', include([
        re_path(r'^$', Timetable.as_view()),
        re_path(r'^(?P<slot_id>\d+)/', include([
            re_path(r'^$', TimetableSlot.as_view())
        ]))
    ])),
    re_path(r'^track-seed/', TrackSeed.as_view())
]
