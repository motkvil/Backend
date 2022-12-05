from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Category2
from .serializers import Category2Serializers


class Category2View(APIView):

    

    def get(self, request):

        

        try:

            Categories = Category2.objects.all()
            serialized = Category2Serializers(Categories, many=True)

            category = Category2.objects.first()
            

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
    
    

        