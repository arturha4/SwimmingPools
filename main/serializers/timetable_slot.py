from datetime import datetime, date, time, timedelta

from rest_framework import serializers

from main.models.timetable_slot import TimetableSlot


def _get_session(start_date, i):
    t = (start_date + timedelta(minutes=45 * i)).time()
    return t.hour, t.minute


def _fits_in_session(start, end):
    """
    попадает ли в сеанс по 45 минут, начиная с 6:30
    https://sport.urfu.ru/activity/sportivnye-sooruzhenija/bassein-universitetskii/
    """
    # мощный хак чтобы прибавлять минуты
    start_date = datetime.combine(
        date.today(),
        time(hour=6, minute=30)
    )
    sessions = [(
        _get_session(start_date, i),
        _get_session(start_date, i + 1)
    ) for i in range(20)]

    return start.hour in [i[0][0] for i in sessions]\
        and start.minute in [i[0][1] for i in sessions]\
        and end.hour in [i[1][0] for i in sessions]\
        and end.minute in [i[1][1] for i in sessions]


class TimetableSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimetableSlot
        fields = ('start', 'end', 'user', 'track')

    def validate(self, attrs):
        # начало должно быть раньше конца
        if attrs['start'] >= attrs['end']:
            raise serializers.ValidationError('начало должно быть раньше окончания')
        # Часы работы: 6:30–22:00, cеансы по 45 минут
        if not _fits_in_session(attrs['start'], attrs['end']):
            raise serializers.ValidationError('время не входит в границы сеанса')
        return attrs
