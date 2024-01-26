from django.urls import path

from .views import CreateSensor, ListSensor, UpdateSensor, MeasurementCreate, GetInfoSensor

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', CreateSensor.as_view()),
    path('listsensors/', ListSensor.as_view()),
    path('updatesensor/<int:pk>/', UpdateSensor.as_view()),
    path('measurements/', MeasurementCreate.as_view()),
    path('sensors/<int:pk>/', GetInfoSensor.as_view()),
]
