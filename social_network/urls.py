from django.urls import path
from .views import SocialNetworkView, SocialNetworkViewSafety

urlpatterns = [
    path('', SocialNetworkView.as_view()),
    path('new/', SocialNetworkViewSafety.as_view()),
]
