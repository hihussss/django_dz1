from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE,blank=True,null=True, related_name='measurements')
    temperature = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)


    def __str__(self):
        return f"{self.temperature}  {self.created_at}  {self.sensor}"

