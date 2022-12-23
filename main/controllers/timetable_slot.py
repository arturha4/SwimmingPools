from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers.timetable_slot import TimetableSlotSerializer
from main.models.timetable_slot import TimetableSlot as TimetableSlotModel


class TimetableSlot(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, slot_id):
        """
        выдать подробности по слоту (здесь будут все related сущности)
        """
        slot_query = TimetableSlotModel.objects.select_related('user', 'track')
        slot = get_object_or_404(slot_query, pk=slot_id)
        serializer = TimetableSlotSerializer(slot)
        return Response(serializer.data, status=status.HTTP_200_OK)
