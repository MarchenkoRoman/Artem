from django.views.generic import RedirectView
from django.urls import path, include

urlpatterns = [
    path('', RedirectView.as_view(url='/hide_information/', permanent=True)),
    path('hide_information/', include('hide_information.urls')),
]
