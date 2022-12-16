from rest_framework.response import Response
from rest_framework.views import APIView

from main.models.timetableSlot import TimetableSlot


class Timetable(APIView):
    # todo
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        return TimetableSlot.objects.get()

    def post(self, request):
        data = request.data
        return Response(TimetableSlot.objects.create(data))
