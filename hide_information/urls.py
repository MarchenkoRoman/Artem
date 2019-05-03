from django.urls import path
from . import views


app_name = 'hide_information'

urlpatterns = [
    path('', views.get_info, name='get_info'),
]
