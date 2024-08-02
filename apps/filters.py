import django_filters
from .models import Ticket
from django import forms

class TicketFilter(django_filters.FilterSet):
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Цена от')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Цена до')
    start_date = django_filters.DateFilter(field_name='event_date', lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date'}), label='Дата от')
    end_date = django_filters.DateFilter(field_name='event_date', lookup_expr='lte', widget=forms.DateInput(attrs={'type': 'date'}), label='Дата до')

    class Meta:
        model = Ticket
        fields = ('price__gt', 'price__lt', 'start_date', 'end_date')
