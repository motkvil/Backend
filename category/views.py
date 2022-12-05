from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Category
from .serializers import CategorySerializers


class CategoryView(APIView):
    def get(self, request):

        try:

            Categories = Category.objects.all()
            serialized = CategorySerializers(Categories, many=True)

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
    
    

        