from rest_framework import serializers

from main.models.timetable_slot import Visitor


class VisitorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ('id', 'name', 'ticket_type')
