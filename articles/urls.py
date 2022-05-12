from django.urls import path
from .views import *

urlpatterns = [
    path('new_article/', CreateArticle.as_view(), name='new_article'),
    path('update_article/<int:pk>', EditArticle.as_view(), name='update_article'),
    path('<int:pk>/', SingleArticleView.as_view(), name='article_detail'),

    path('del_article/<int:pk>', ArticleDeleteView.as_view(), name='del_article'),

]