from django.urls import re_path, include, path

from main.controllers.sessions import SessionView
from main.controllers.time_choices import TimeChoices
from main.controllers.timetable import Timetable
from main.controllers.timetable_slot import TimetableSlot, TracksSchedule, UpcomingTimetableSlot, SlotStatusDetail
from main.controllers.track_seed import TrackSeed
from main.controllers.tracks import Tracks

urlpatterns = [
    re_path(r'^timetable/', include([
        re_path(r'^$', Timetable.as_view()),
        re_path(r'^(?P<slot_id>\d+)/', include([
            re_path(r'^$', TimetableSlot.as_view())
        ])),
        re_path(r'^time-choices/', TimeChoices.as_view())
    ])),
    re_path(r'^track-seed/',    TrackSeed.as_view()),
    path('tracks/', Tracks.as_view()),
    path('tracks-schedule/', TracksSchedule.as_view()),
    path('upcoming-slots/', UpcomingTimetableSlot.as_view()),
    path('session/', SessionView.as_view()),
    path('slot-payment/<int:pk>/', SlotStatusDetail.as_view())
]
