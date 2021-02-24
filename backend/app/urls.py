from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from graphene_django.views import GraphQLView
from rest_framework.routers import DefaultRouter
from . import views
from .views import *
router = DefaultRouter()
router.register('posts',PostViewSet, basename='posts')
router.register('saves',SaveViewSet, basename='saves')
router.register('shares',ReportViewSet, basename='shares')
router.register('comments',CommentViewSet, basename='comments')
router.register('likes',LikeViewSet, basename='likes')
router.register('dialogs',DialogViewSet, basename='dialogs')
router.register('messages',MessageViewSet, basename='messages')
router.register('simpleUsers', SimpleUserViewSet, basename='simpleuser')


app_name = "app"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path('api/v1/', include(router.urls)),
]
