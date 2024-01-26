from django_filters import rest_framework as filters
from django_filters.filters import DateFromToRangeFilter


from advertisements.models import Advertisement, AdvertisementStatusChoices


class DateFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    date = filters.DateFromToRangeFilter()
    

    
    class Meta:
        model = Advertisement
        fields = ['creator', 'date' ]

class StatusFilter(filters.FilterSet):
    choise = filters.ChoiceFilter(field_name='status', choices=AdvertisementStatusChoices) 

    class Meta:
        model = Advertisement
        fields = ('created_at',)        