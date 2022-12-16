from django.contrib.auth.models import User
from django.db import models


class TimetableSlot(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def intersects_with_slot(self, slot):
        """если слоты пересекаются то создать новый нельзя"""
        return slot.start <= self.end or self.start <= slot.end

    def is_correct(self):
        """начало должно быть раньше конца"""
        return self.start < self.end
