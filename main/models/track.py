from django.db import models
from django.db.models import Sum

track_capacity = 8


class Track(models.Model):
    """номер дорожки, чтобы он был независим от autoincremented id"""
    TRACK_CHOISE = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6)
    )
    number = models.IntegerField(choices=TRACK_CHOISE)

    def get_people(self):
        return self.objects.select_related()

    def get_count_of_visitors(self, date, time_slot):
        visitors = self.slots.filter(date=date, time_slot=time_slot).aggregate(Sum('visitors'))[
            'visitors__sum']
        if visitors is None:
            return 0
        return visitors

    def available(self, date, time_slot, visitors):
        counted_people = self.get_count_of_visitors(date, time_slot)
        if counted_people + visitors > track_capacity:
            return False
        return True
