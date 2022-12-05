from django.urls import path
from .viewsArticle import ArticleView, ArticleViewFiltered, ArticleInstance, CommentView

urlpatterns = [
    path('', ArticleView.as_view()),
    path('filter/', ArticleViewFiltered.as_view()),
    path('get/', ArticleInstance.as_view()),
    path('comment/', CommentView.as_view()),

]
