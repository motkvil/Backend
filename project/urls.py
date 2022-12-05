from django.urls import path
from .views import ProjectView, ProjectViewSafety

urlpatterns = [
    path('', ProjectView.as_view()),
    path('new/', ProjectViewSafety.as_view()),
]
