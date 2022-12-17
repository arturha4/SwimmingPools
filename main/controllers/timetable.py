from datetime import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models.timetableSlot import TimetableSlot


class Timetable(APIView):
    # todo
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        return Response(TimetableSlot.objects.all(), status.HTTP_200_OK)

    def post(self, request):
        # перепишу на сериализаторах потом
        # создает слот и возвращает результат его правильности
        # все равно записывает, даже если невалидный, потом доделаю
        data = request.data
        timetable_slot = TimetableSlot.objects.create(**data)
        start = datetime.fromisoformat('2022-12-17T19:06:07')
        end = datetime.fromisoformat('2022-12-17T21:06:07')

        intersects = timetable_slot.intersects_with_slot({'start': start, 'end': end})
        correct = timetable_slot.is_correct()
        return Response(
            {
                'intersects': intersects,
                'correct': correct,
            },
            status.HTTP_200_OK
        )
