# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response


from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer,SensorDetailSerializer
# Create Sensor
class CreateSensor(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
# List Sensors
class ListSensor(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# Update Sensor
class UpdateSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
# Create Measurement
class MeasurementCreate(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
# Get Info Sensor
class GetInfoSensor(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

