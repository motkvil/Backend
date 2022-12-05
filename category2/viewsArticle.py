from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import serializers, status


from .models import Article, Category2, Comment
from .serializers import ArticleSerializers, Category2Serializers, CommentSerializers


class ArticleView(APIView):

    def get(self, request):

        try:

            articulos = Article.objects.all()
            serialized = ArticleSerializers(articulos, many=True)
            

            return Response(
                status = status.HTTP_200_OK,
                data = {
                    "multipass" : True,
                    "data": serialized.data
                }
              )
        except:

          return Response(
              status=status.HTTP_400_BAD_REQUEST,
              
          )
    
    def post(self, request):

        try:

            
            try:

                data = request.data
                serialized = ArticleSerializers(data=data)

                if serialized.is_valid():
                    serialized.save()

                    return Response(
                        status = status.HTTP_200_OK,
                        data={
                            "multipass":True,
                            "data": {
                                "article": serialized.data,
                            }
                        }
                    )
                
                else:
                    return Response(
                        status = status.HTTP_400_BAD_REQUEST,
                        data={
                            "multipass":False,
                            "detail": serialized.errors
                        }
                    )
                
                

            except:

                return Response(
                    status= status.HTTP_400_BAD_REQUEST,
                    data={
                        "multipass": False,
                        "detail": "No funciono"
                    }
                )
            
            
        
        except:

            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "multipass": False,
                }
            )


class ArticleViewFiltered(APIView):
    
    def get(self, request):

        try:
            
            try:
                categoryId = request.query_params.get('category')
                category = Category2.objects.get(id=categoryId)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND,data={
                    "multipass": False,
                    "detail": "Categoria no encontrada"
                })

            articles = category.article.all()
            serializedC = Category2Serializers(category)
            serialized = ArticleSerializers(articles, many=True)

            return Response(
                status= status.HTTP_200_OK,
                data={
                    "multipass" : True,
                    "data": serialized.data,
                    "category": serializedC.data,
                }
            )
            
        except:
            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )


class ArticleInstance(APIView):

    def get (self, request):
        try:

            try:
                articleId = request.query_params.get('instance')
                post = Article.objects.get(id=articleId)
                categories = post.categories.all()
                serializedCategory = Category2Serializers(categories, many=True)
                serialized = ArticleSerializers(post)

                return Response(
                    status=status.HTTP_200_OK,
                    data={
                        "multipass": True,
                        "data": serialized.data,
                        "category": serializedCategory.data
                    }
                )
            
            except:

                return Response(
                    status=status.HTTP_404_NOT_FOUND,
                    data={
                        "multipass": False,
                        "detail": "No article found"
                    }
                )

        except:

            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )


class CommentView(APIView):

    def post(self, request):

        try:

            
            try:

                articleId = request.query_params.get('article')

                article = Article.objects.get(id=articleId)
                comment = Comment.objects.create(
                    content=request.data['content'], 
                    alias= request.data['alias']
                )

                article.comment.add(comment)
                serializedA = ArticleSerializers(article)
                serializedC = CommentSerializers(comment)

                return Response(
                    status = status.HTTP_200_OK,
                    data={
                        "multipass":True,
                        "data": {
                            "article": serializedA.data,
                            "comment": serializedC.data
                        }
                    }
                )
                
                

            except:

                return Response(
                    status= status.HTTP_400_BAD_REQUEST,
                    data={
                        "multipass": False,
                        "detail": "No funciono"
                    }
                )
            
            
        
        except:

            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "multipass": False,
                }
            )

    def get(self, request):

        try:
            articleId = request.query_params.get('article')

            try:
                article = Article.objects.get(id=articleId)
                comments = article.comment.all()
                serialized = CommentSerializers(comments, many=True)

                return Response(
                status = status.HTTP_200_OK,
                data= {
                    "multipass" : True,
                    "data": serialized.data
                }
            )
            
            except:
                return Response(
                status = status.HTTP_404_NOT_FOUND,
                data= {
                    "multipass" : False,
                    "data": "Article not found"
                }
            )
            return Response(
                status = status.HTTP_200_OK,
                data= {
                    "multipass" : True,
                    "data": "ok"
                }
            )
        except:

            return Response(
                status = status.HTTP_400_BAD_REQUEST,
                data= {
                    "multipass" : False,
                    "data": "Nop"
                }
            )


