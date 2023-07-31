from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('specific', views.specific, name='specific'),
        path('getResponse', views.getResponse,name='getResponse'),


    # path ('article/<int:article_id>', views.article, name='article_id')
]
