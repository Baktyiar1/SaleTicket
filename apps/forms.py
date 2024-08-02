from django import forms
from .models import Ticket


class TicketUpdateform(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = (
            'title',
            'description',
            'price',
            'location_event',
            'image',
            'event_date',
            'date_duration',
            'quantity'
        )