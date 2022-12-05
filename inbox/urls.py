from django.urls import path
from .views import EmailView, EmailViewSafety

urlpatterns = [
    path('', EmailView.as_view()),
    path('new/', EmailViewSafety.as_view()),
]
