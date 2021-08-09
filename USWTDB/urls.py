from django.urls import path
from .views import WindMill, Graph

urlpatterns = [
    path('', WindMill.wind_view),
    path('map/',Graph.as_view()),
]
