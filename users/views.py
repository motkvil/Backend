from django.contrib.auth.models import User
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import CustomUserModel, Notification, Context
from .serializers import CustomUserSerializer, NotificationSerializer

import os
import jwt

class CustomUser(APIView):

    def post(self,request):
        data = request.data
        serialized = CustomUserSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            user = CustomUserModel.objects.get(username=data['username'])
            user.set_password(data['password'])
            user.save()

            return Response(
                data=serialized.data,
                status=status.HTTP_200_OK
            )



        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serialized.errors
        )
    
    def get(self, request):

        try:


            try:

                requestUser = request.user
                requestUser.is_superuser
                serialized = CustomUserSerializer(requestUser)

                return Response(
                    status=status.HTTP_200_OK,
                    data={
                        "multipass": True,
                        "detail": "User detected",
                        "data": serialized.data,
                        "isAdmin": requestUser.is_superuser
                    }
                )
                
            except:
                return Response(
                    status=status.HTTP_401_UNAUTHORIZED,
                    data={
                        "multipass": False,
                        "detail": "NO information"
                    }
                )

            

                

            
        except:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )


class NotificationView(APIView):

    def get(self, request):

        try:


            try:
                token = request.headers['authorization'].split(" ")[1]
                decode = jwt.decode(token, os.getenv('SECRET'))

                
            except:
                return Response(
                    status=status.HTTP_401_UNAUTHORIZED,
                    data={
                        "multipass": False,
                        "detail": "NO information"
                    }
                )

            user = CustomUserModel.objects.get(id=decode['user_id'])

            Client = Context.objects.get(name="Client")
            Admin = Context.objects.get(name="Admin")
            System = Context.objects.get(name="System")

            notificationsAdmin = Notification.objects.filter(to=user,context=Admin)
            notificationsSystem = Notification.objects.filter(context=System, to=user)
            notificationsClient = Notification.objects.filter(to=user, context=Client)

            serializedAdmin = NotificationSerializer(notificationsAdmin, many=True)
            serializedSystem = NotificationSerializer(notificationsSystem, many=True)
            serializedClient = NotificationSerializer(notificationsClient, many=True)


            
            if user.is_superuser:
                return Response(
                    status=status.HTTP_200_OK,
                    data={
                        "multipass": True,
                        "detail": "Notificaciones Para administrador",
                        "data": {
                            "client": serializedClient.data,
                            "system": serializedSystem.data,
                            "admin": serializedAdmin.data
                        }
                    }
                )
            else:
               
                print()
                return Response(
                    status=status.HTTP_200_OK,
                    data={
                        "multipass": True,
                        "detail": "Notificaciones para usuario",
                        "data": serializedClient.data
                    }
                )
        except:
            return Response(
                status=status.HTTP_400_BAD_REQUEST 
            )


class NotificationUnsubscribeView(APIView):

    def post(self, request):

        try:

            try:
                token = request.headers['authorization'].split(" ")[1]
                decode = jwt.decode(token, os.getenv('SECRET'))

                
            except:
                return Response(
                    status=status.HTTP_401_UNAUTHORIZED,
                    data={
                        "multipass": False,
                        "detail": "NO information"
                    }
                )

            user = CustomUserModel.objects.get(id=decode['user_id'])

            try:
                notificacion = Notification.objects.get(id=request.data['id'])
                notificacion.to.remove(user)

                return Response(
                    status=status.HTTP_204_NO_CONTENT,
                    data={
                        "multipass": True,
                        "detail": "Notificacion desmarcada"
                    }
                )
            except:

                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={
                        "multipass": False,
                        "detail": "No given data",
                    }
                )

            

        except:

            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "multipass": False,
                    "detail": "Somethint went wrong",
                }
            )