from django.urls import path, include
from . import views

app_name = "contact_tracing"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path('stat_search/', views.stat_search, name='stat_search'),
    path('ajax/load-rooms/', views.load_rooms, name='ajax_load_rooms'),
    path('get_data', views.get_data, name='get_data'),
]