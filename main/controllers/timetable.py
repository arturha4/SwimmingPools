from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models.timetable_slot import TimetableSlot
from main.serializers.timetable_slot import TimetableSlotSerializer


class Timetable(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        получить расписание текущего юзера
        """
        my_slots = TimetableSlot.objects.filter(user_id=request.user.id)
        serializer = TimetableSlotSerializer(my_slots, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = TimetableSlotSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            # потом проверить что чел уже записывался на это время, что не превышено колво людей на дорожку итд
            data = serializer.validated_data
            serializer.save()
            return Response(
                serializer.data,
                status.HTTP_200_OK
            )
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
