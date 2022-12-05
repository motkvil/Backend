from django.contrib.auth.models import User
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import TunnelEvent, Tunnel
from .serializers import TunnelSerializer, TunnelEventSerializer


class TunnelView(APIView):

  def get(self, request):

    try:
      return Response(
        status=status.HTTP_200_OK,
        data={
          "multipass": True,
        }
      )
    except:

      return Response(
        status=status.HTTP_400_BAD_REQUEST,
        data={
          "multipass": False,
          "detail": "No data"
        }
      )