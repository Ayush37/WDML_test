from django.urls import path
from .views import WindMill

urlpatterns = [
    path('', WindMill.wind_view),
]
