import datetime
from typing import Self

from django.contrib.auth.models import User
from django.db import models


def _get_session(start_date, i):
    t = (start_date + datetime.timedelta(minutes=45 * i)).time()
    return t.hour, t.minute


def _str2datetime(s) -> datetime.datetime:
    return datetime.datetime.fromisoformat(s)


class TimetableSlot(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def intersects_with_slot(self, slot: [Self]):
        """если слоты пересекаются то создать новый нельзя"""
        return slot['start'] <= _str2datetime(self.end) or _str2datetime(self.start) <= slot['end']

    def is_correct(self):
        # начало должно быть раньше конца
        start_earlier_end = self.start < self.end
        # Часы работы: 6:30–22:00, cеансы по 45 минут
        in_open_hours = self._fits_in_session()
        return start_earlier_end and in_open_hours

    def _fits_in_session(self):
        """
        попадает ли в сеанс по 45 минут, начиная с 6:30
        https://sport.urfu.ru/activity/sportivnye-sooruzhenija/bassein-universitetskii/
        """
        # мощный хак чтобы прибавлять минуты
        start_date = datetime.datetime.combine(
            datetime.date.today(),
            datetime.time(hour=6, minute=30)
        )
        sessions = [(
            _get_session(start_date, i),
            _get_session(start_date, i + 1)
        ) for i in range(20)]

        return _str2datetime(self.start).hour in [i[0][0] for i in sessions]\
            and _str2datetime(self.start).minute in [i[0][1] for i in sessions]\
            and _str2datetime(self.end).hour in [i[1][0] for i in sessions]\
            and _str2datetime(self.end).minute in [i[1][1] for i in sessions]
