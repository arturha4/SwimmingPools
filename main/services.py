from datetime import datetime as dt, timedelta
from django.db.models import Sum

from main.models.timetable_slot import TimetableSlot, TIME_CHOICES


def get_empty_schedule(start, end):
    return {(start + timedelta(date)).strftime('%Y-%m-%d'): {choice[0]: 8 for choice in TIME_CHOICES} for date in range(int((end - start).days) + 1)}


def get_booked_tracks_by_datetime(start_date: str, end_date: str, visitors_limit: int = 8):
    return TimetableSlot.objects.select_related('track').filter(date__range=(start_date, end_date)).values('date',
                                                                                                           'time_slot',
                                                                                                           'track__number').annotate(
        visitors_sum=Sum('visitors')).filter(visitors_sum__gte=visitors_limit)


def get_count_of_available_tracks_by_datetime(start_date: str, end_date: str):
    schedule = get_empty_schedule(dt.strptime(start_date, '%Y-%m-%d').date(), dt.strptime(end_date, '%Y-%m-%d').date())
    busy_slots = get_booked_tracks_by_datetime(start_date, end_date)
    for item in busy_slots:
        schedule[item['date'].strftime('%Y-%m-%d')][item['time_slot']] -= 1
    return schedule
