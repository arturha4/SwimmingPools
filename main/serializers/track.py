from rest_framework import serializers

from main.models.track import Track


class TrackAvailableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'number']

# здесь можно приделать колво доступных для записи мест...
