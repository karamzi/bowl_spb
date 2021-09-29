from rest_framework import serializers
from tournaments.models import Calendar, Regulation


class CalendarSerializer(serializers.ModelSerializer):
    regulation = serializers.SerializerMethodField()

    def get_regulation(self, obj: Calendar):
        if obj.regulation:
            return obj.regulation.file.url
        return ''

    class Meta:
        model = Calendar
        fields = ['id', 'competition', 'city', 'status', 'date_start', 'date_finish', 'regulation']
        depth = 0
