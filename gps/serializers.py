from rest_framework import serializers
from .models import GPS, GPSCheck

class GPSSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPS
        fields = ('id', 'user_id', 'created_at', 'longitude', 'latitude',)

class GPSCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPSCheck
        fields = ('user', 'other', 'times')
