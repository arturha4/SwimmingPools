from datetime import datetime
from rest_framework import serializers

from main.models.timetable_slot import TimetableSlot


def valid_datetime_slot(date, slot_time):
    time = datetime.strptime(slot_time, '%H:%M').time()
    date = datetime.combine(date, time)
    if date < datetime.now():
        raise serializers.ValidationError('Некорректная дата и время для записи')
    return True


class TimetableSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimetableSlot
        fields = '__all__'

    def validate(self, attrs):
        if not attrs['track'].available(date=attrs['date'], time_slot=attrs['time_slot'], visitors=attrs['visitors']):
            raise serializers.ValidationError('Свободных мест для такого кол-ва людей не осталось')
        if attrs['user'].have_slot():
            raise serializers.ValidationError('Отмените прошлую запись')
        if not valid_datetime_slot(attrs['date'], attrs['time_slot']):
            raise serializers.ValidationError('Некорректная дата записи')
        return attrs
