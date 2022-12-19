from django.db import models


class Track(models.Model):
    def get_people(self):
        return self.objects.select_related()
