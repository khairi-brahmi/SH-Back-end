from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import viewsets
from rest_framework import permissions
from .models import *
from .serializers import *
from .filters import *
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework import exceptions
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, RedirectView, DeleteView, UpdateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import *
from rest_framework import filters


@api_view()
def null_view(request):
    return Response(status=status.HTTP_400_BAD_REQUEST)

class HomePageView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
class SimpleUserViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == "create":
            return SimpleUserUserCreateSerializer
        else:
            return SimpleUserSerializer
    
    def get_queryset(self):
       # user = self.request.user
       
        return SimpleUser.objects.all()
    
"""  def get_permissions(self):
        if self.action in ["create"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes] """
    
    #filterset_class = 
class PostViewSet(viewsets.ModelViewSet):
    search_fields = ['about']
    filter_backends = (filters.SearchFilter,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_class = PostFilter
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
class ReportViewSet(viewsets.ModelViewSet):
    queryset = ReportPost.objects.all()
    serializer_class = ReportSerializer
class SaveViewSet(viewsets.ModelViewSet):
    queryset = SavePost.objects.all()
    serializer_class = SaveSerializer
    filterset_class =SaveFilter
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_date').reverse()
    serializer_class = CommentSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-sent_at')
    serializer_class = MessageSerializer
    #filterset_class =MessageFilter
class DialogViewSet(viewsets.ModelViewSet):
    queryset = Dialog.objects.all()
    serializer_class = DialogSerializer
    filterset_class =DialogFilter