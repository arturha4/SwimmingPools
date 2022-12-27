import datetime

from django.db.models import Count, Sum

from swimmigPool import settings
from django.db import models

from main.models.track import Track


def _str2datetime(s) -> datetime.datetime:
    return datetime.datetime.fromisoformat(s)


TIME_CHOICES = (
        ('6:30', '7:15'),
        ('7:15', '8:00'),
        ('8:00', '8:45'),
        ('8:45', '9:30'),
        ('9:30', '10:15'),
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


def available_tracks_by_date(date, time_slot):
    """
    Возвращает дорожки с кол-ом занятых мест в формате:
    [{'track': 2, 'visitors__sum': 6}, {'track': 5, 'visitors__sum': 3}, {'track': 6, 'visitors__sum': 5}]>
    """
    return TimetableSlot.objects.select_related('track').filter(date=date, time_slot=time_slot).values('track').annotate(Sum('visitors'))
