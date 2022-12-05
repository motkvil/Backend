from django.urls import path
from .views import LanguageView, LanguageViewSafety

urlpatterns = [
    path('', LanguageView.as_view()),
    path('new/', LanguageViewSafety.as_view()),
]
