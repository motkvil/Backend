from django.contrib.auth.models import User
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import (IsAdminUser, IsAuthenticated)

from users.models import Notification, CustomUserModel
from users.serializers import NotificationSerializer

from users.models import Context

from .models import Email
from .serializers import EmailSerializer

import os
import jwt

class EmailView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self, request):

        try:

            Emails = Email.objects.all()
            serialized = EmailSerializer(Emails, many=True)
            return Response(
                status = status.HTTP_200_OK,
                data = {
                    "multipass" : True,
                    "data" : serialized.data
                }
            )
        except:
            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )


class EmailViewSafety(APIView):
    def post(self,request):
        data = request.data
        serialized = EmailSerializer(data=data)

        try:

            token = request.headers['authorization'].split(" ")[1]
            decode = jwt.decode(token, os.getenv('SECRET'))
            user = CustomUserModel.objects.get(id=decode["user_id"])

            if serialized.is_valid():
                context = Context.objects.get(name="Admin")
                admins = CustomUserModel.objects.filter(is_superuser=True)

                newNoti = Notification.objects.create(
                    description= str(user.username) +", dejó un correo en el buzon público", 
                    title="Nuevo mensaje de "+ str(user.username).upper(),
                    host=user, 
                    context=context
                )
                for items in admins:
                    newNoti.to.add(items)
                newNoti.save()
                serialized.save()

                return Response(
                    data=serialized.data,
                    status=status.HTTP_200_OK
                )

            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serialized.errors
            )

            
        except:
            if serialized.is_valid():
                context = Context.objects.get(name="Admin")
                host = CustomUserModel.objects.first()
                admins = CustomUserModel.objects.filter(is_superuser=True)

                newNoti = Notification.objects.create(
                    description="Alguin dejó un correo en el buzon publico", 
                    title="Nuevo mensaje en el buzon",  
                    host=host, 
                    context=context
                )
                for items in admins:
                    newNoti.to.add(items)
                newNoti.save()
                newNoti.save()
                serialized.save()
                return Response(
                    data=serialized.data,
                    status=status.HTTP_200_OK
                )

            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serialized.errors
            )


        