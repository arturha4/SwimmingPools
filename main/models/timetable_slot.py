import datetime

from django.db.models import Sum

from swimmigPool import settings
from django.db import models

from main.models.track import Track, track_capacity


def _str2datetime(s) -> datetime.datetime:
    return datetime.datetime.fromisoformat(s)


TIME_CHOICES = (
        ('06:30', '07:15'),
        ('07:15', '08:00'),
        ('08:00', '08:45'),
        ('08:45', '09:30'),
        ('09:30', '10:15'),
        ('10:15', '11:00'),
        ('11:45', '12:30'),
        ('12:30', '13:15'),
        ('13:15', '14:00'),
        ('14:00', '14:45'),
        ('14:45', '15:30'),
        ('15:30', '16:15'),
        ('16:15', '17:00'),
        ('17:00', '17:45'),
        ('17:45', '18:30'),
        ('18:30', '19:15'),
        ('19:15', '20:00'),
        ('20:00', '20:45'),
        ('20:45', '21:30'),
    )



class TimetableSlot(models.Model):
    date = models.DateField()
    time_slot = models.CharField(max_length=5, choices=TIME_CHOICES)
    # 1 user - many slots
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='slots')
    # 1 track - many slots
    track = models.ForeignKey(Track, on_delete=models.CASCADE, null=True, related_name='slots')
    visitors = models.IntegerField()

    def __str__(self):
        return f'Дорожка: {self.track.number}, Дата: {self.date} Время сеанса: {self.time_slot}, Посетителей {self.visitors}'



