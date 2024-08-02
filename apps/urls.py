from django.urls import path
from . import views

urlpatterns = [
    path('',views.index_views, name='index'),
    path('detail/<int:pk>/',views.event_detail,name='detail'),
    path('profile/',views.profile_views, name='profile'),
    path('list/',views.event_listing,name='list'),
    path('event_create/',views.event_create_views,name='create'),

]
