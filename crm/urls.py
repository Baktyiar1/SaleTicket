from django.urls import path
from . import views

urlpatterns = [
    path('event_list/',views.event_crm_list,name='list_crm'),

]
