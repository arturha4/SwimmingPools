from rest_framework import serializers
from main.serializers.visitor import VisitorsSerializer
from main.models.timetable_slot import SwimmingSession, Visitor


class SwimmingSessionSerializer(serializers.ModelSerializer):
    visitors = VisitorsSerializer(many=True)

    class Meta:
        model = SwimmingSession
        fields = "__all__"

    def create(self, validated_data):
        session = SwimmingSession.objects.create(timetable_slot_id=validated_data.pop('timetable_slot').id)
        objs = [Visitor(
            name=v["name"],
            ticket_type=v['ticket_type'],
            session_id=session.id) for v in validated_data.pop('visitors')]
        Visitor.objects.bulk_create(objs)
        return session
