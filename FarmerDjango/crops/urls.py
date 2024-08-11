from django.urls import path
from .views import SoilProfileView

urlpatterns = [
    path('recommend/', SoilProfileView.as_view(), name='recommend')
]

