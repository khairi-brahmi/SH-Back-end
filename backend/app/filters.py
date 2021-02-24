import django_filters
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import *
from rest_framework.response import Response



class MessageFilter(filters.FilterSet):
    class Meta:
        model = Message
        fields = {
            'sender': ['exact'],
            'sent_at': ['icontains']
        }
        
class DialogFilter(filters.FilterSet):
    class Meta:
        model = Dialog
        fields = {
            'users': ['exact']
            
        }
class SaveFilter(filters.FilterSet):
    class Meta:
        model = SavePost
        fields = {
            'savedby': ['exact'],
            'postID': ['exact']
            
        }
class PostFilter(filters.FilterSet):
    
    class Meta:
        model = Post
        fields = {
            'publisher': ['exact'],
            'country':['exact'],
            'city':['exact'],
            'kind':['exact'],
            'category':['exact'],
            'saves':['exact']
            
        }
