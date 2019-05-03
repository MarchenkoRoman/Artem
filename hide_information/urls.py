from django.urls import path
from . import views


app_name = 'hide_information'

urlpatterns = [
    path('', views.hide_info, name='hide_info'),
]
