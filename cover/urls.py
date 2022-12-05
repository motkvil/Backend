from django.urls import path
from .views import CoverView, CoverViewSafety

urlpatterns = [
    path('', CoverView.as_view()),
    path('new/', CoverViewSafety.as_view())
]
