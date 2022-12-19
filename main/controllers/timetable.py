from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models.timetable_slot import TimetableSlot
from main.serializers.timetable_slot import TimetableSlotSerializer


class Timetable(APIView):
    # todo
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        return Response(TimetableSlot.objects.all(), status.HTTP_200_OK)

    def post(self, request):
        serializer = TimetableSlotSerializer(data=request.data)
        if serializer.is_valid():
            # потом проверить что чел уже записывался на это время, что не превышено колво людей на дорожку итд
            data = serializer.validated_data
            serializer.save()
            return Response(
                'ok)',
                status.HTTP_200_OK
            )
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
