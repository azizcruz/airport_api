from django.urls import path
from . import views

urlpatterns = [
    path('airports/', views.Test.as_view(), name='test')
]