from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models.track import Track


class TrackSeed(APIView):
    def post(self, request):
        """cоздать дорожки, вызывает разраб с постмана"""
        for i in range(1, 9):
            Track.objects.create(**{'number': i})
        return Response('seeding done', status=status.HTTP_200_OK)
