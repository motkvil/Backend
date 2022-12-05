from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserModel, Context, Notification, Tunnel, TunnelEvent

# Register your models here.
admin.site.register(CustomUserModel, UserAdmin)
admin.site.register(Context)
admin.site.register(Notification)
admin.site.register(Tunnel)
admin.site.register(TunnelEvent)