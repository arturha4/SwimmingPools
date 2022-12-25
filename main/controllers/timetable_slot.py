from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers.timetable_slot import TimetableSlotSerializer
from main.models.timetable_slot import TimetableSlot as TimetableSlotModel


class TimetableSlot(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, slot_id):
        """
        выдать подробности по слоту (здесь будут все related сущности)
        """
        slot_query = TimetableSlotModel.objects.select_related('user', 'track')
        slot = get_object_or_404(slot_query, pk=slot_id)
        serializer = TimetableSlotSerializer(slot)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, slot_id):
        """
        удалить слот по его id
        """
        slot = TimetableSlotModel.objects.get(id=slot_id)
        slot.delete()
        return Response(data="Удалено", status=status.HTTP_204_NO_CONTENT)


class TracksSchedule(APIView):
    permission_classes = []
    def get(self, request):
        """
        Возвращает слоты за определенный промежуток времени, берущийся из параметров запроса
        """
        start, end = request.GET.get('start'), request.GET.get('end')
        serializer = TimetableSlotSerializer(TimetableSlotModel.objects.filter
                                             (date__range=[start, end]).order_by('date'), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
