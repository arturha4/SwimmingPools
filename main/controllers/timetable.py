from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models.timetable_slot import TimetableSlot
from main.serializers.timetable_slot import TimetableSlotSerializer


class Timetable(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        получить расписание текущего юзера
        """
        my_slots = TimetableSlot.objects.filter(user_id=request.user.id)
        serializer = TimetableSlotSerializer(my_slots, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        request.data['user'] = request.user.id
        serializer = TimetableSlotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


