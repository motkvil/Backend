from django.contrib.auth.models import User
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import (IsAdminUser, IsAuthenticated)

from .models import Cover
from .serializers import CoverSerializer

import os
import jwt

class CoverView(APIView):
    def get(self, request):

        try:

            covers = Cover.objects.all()
            serialized = CoverSerializer(covers, many=True)
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


class CoverViewSafety(APIView):
    permission_classes = (IsAdminUser,)
    def post(self,request):
        data = request.data
        serialized = CoverSerializer(data=data)

        if serialized.is_valid():
            serialized.save()
            return Response(
                data=serialized.data,
                status=status.HTTP_200_OK
            )

        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serialized.errors
        )