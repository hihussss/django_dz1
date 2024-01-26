from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
# from django_filters import DateFromToRangeFilter
from .models import Advertisement
from .serializers import AdvertisementSerializer
from .filters import DateFilter, StatusFilter
from .permission import IsOwner

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['creator',]
    filterset_class = DateFilter
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        
    
    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    # def get_permissions(self):
    #     """Получение прав для действий."""
    #     if self.action in ["create", "update", "partial_update", "destroy"]:
    #         return [IsAuthenticated()]
    #     return []
