from django.urls import path
from . import views

urlpatterns = [
    path('airports/', views.ListAirports.as_view(), name='list-all'),
    path('airports/iata_code/<str:iata_code>/', views.IATA_search.as_view(), name='search-iata_code'),
    path('airports/search_name/<str:name>/', views.NameFilter.as_view(), name='name-filter'),
]