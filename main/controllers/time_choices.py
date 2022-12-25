from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models.timetable_slot import TIME_CHOICES


class TimeChoices(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'timeChoices': TIME_CHOICES}, )
