from django.urls import path
from .views import AntimatterView, UnityView

urlpatterns = [
    path('', AntimatterView.as_view()),
    path('new/', AntimatterView.as_view()),
    path('unities/', UnityView.as_view()),
]   
