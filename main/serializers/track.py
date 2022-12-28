from rest_framework import serializers

from main.models.track import Track


class TrackAvailableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'number', 'available_places']

    def get_available_places(self):
        pass
# здесь можно приделать колво доступных для записи мест...
