from rest_framework import serializers
from .models import Sensor, Measurement
# TODO: опишите необходимые сериализаторы


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = (['temperature', 'created_at','image'])
        depth = 1
class SensorSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']        
class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True, read_only=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
        
    