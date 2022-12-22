from django.db import models


class Track(models.Model):
    """номер дорожки, чтобы он был независим от autoincremented id"""
    number = models.IntegerField()

    def get_people(self):
        return self.objects.select_related()
