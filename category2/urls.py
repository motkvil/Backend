from django.urls import path
from .views import Category2View

urlpatterns = [
    path('', Category2View.as_view()),
]
