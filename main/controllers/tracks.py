from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models.track import Track as TrackModel
from main.serializers.track import TrackAvailableSerializer


class Tracks(APIView):
    def get(self, request):
        time_slot, new_visitors = request.GET.get('time_slot'), request.GET.get('new_visitors')
        all_tracks = TrackModel.objects.all()
        available = [track for track in all_tracks if track.available(time_slot, new_visitors)]
        serializer = TrackAvailableSerializer(available, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
