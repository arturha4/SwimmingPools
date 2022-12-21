import datetime
from swimmigPool import settings
from django.db import models

from main.models.track import Track


def _str2datetime(s) -> datetime.datetime:
    return datetime.datetime.fromisoformat(s)


class TimetableSlot(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    # 1 user - many slots
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    # 1 track - many slots
    track = models.ForeignKey(Track, on_delete=models.CASCADE, null=True)

    def intersects_with_slot(self, slot):
        """если слоты пересекаются то создать новый нельзя"""
        return slot['start'] <= _str2datetime(self.end) or _str2datetime(self.start) <= slot['end']
