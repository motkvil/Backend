from django.urls import path
from .viewsTunnel import TunnelView

urlpatterns = [
    path('', TunnelView.as_view())
]
