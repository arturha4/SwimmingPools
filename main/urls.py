from django.urls import path

from main.controllers.timetable import Timetable

urlpatterns = [
    path('timetable/', Timetable.as_view()),
]
