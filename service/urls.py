from django.urls import path
from .views import ServiceView, ServiceViewSafety

urlpatterns = [
    path('', ServiceView.as_view()),
    path('new/', ServiceViewSafety.as_view()),
]
