from django.urls import path
from .views import NotificationView, NotificationUnsubscribeView

urlpatterns = [
    path('', NotificationView.as_view()),
    path('delete/', NotificationUnsubscribeView.as_view())
]
