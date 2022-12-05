from rest_framework.serializers import ModelSerializer
from .models import CustomUserModel, Notification, TunnelEvent, Tunnel

class CustomUserSerializer(ModelSerializer):
  class Meta:
    model = CustomUserModel
    fields = ('id','username','password','email', 'color', 'image', 'last_login','date_joined')




class NotificationSerializer(ModelSerializer):
  class Meta:
    model = Notification
    fields = ('__all__')




class TunnelSerializer(ModelSerializer):
  class Meta:
    model = Tunnel
    fields = ('__all__')



    

class TunnelEventSerializer(ModelSerializer):
  class Meta:
    model = TunnelEvent
    fields = ('__all__')