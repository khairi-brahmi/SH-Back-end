from rest_framework import serializers
from .models import *
from backend.users.models import User
from allauth.account import app_settings as allauth_settings
from allauth.account.adapter import get_adapter
from allauth.utils import (email_address_exists,
                           get_username_max_length)
from allauth.account.utils import setup_user_email
from django.db.models.functions.datetime import datetime
from django.db.models.functions import ExtractYear
from django.db.models import Avg, Sum
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Like
        fields = ['id','liker', 'postID']
class CommentSerializer(serializers.ModelSerializer):
    auther_name = serializers.ReadOnlyField(source='auther.get_full_name')

    class Meta:
        model= Comment
        fields = ['id','auther','auther_name', 'postID','content','created_date']
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model= ReportPost
        fields = ['id','reportedby', 'postID']
class SaveSerializer(serializers.ModelSerializer):

    class Meta:
        model= SavePost
        fields = ['id','savedby','postID']



class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model= Message
        fields = ['id','dialog','content','sender', 'seen','sent_at']


class PostSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    saves = SaveSerializer(many=True, read_only=True)
    saves_id=serializers.ReadOnlyField(source='saves.savedby')
    reports = ReportSerializer(many=True, read_only=True)
    publisher_name = serializers.ReadOnlyField(source='publisher.get_full_name')
    class Meta:
        model = Post
        fields = ['id', 'date_create','comments','saves_id','likes','publisher_name','reports', 'about','image', 'kind','category','publisher', 'city', 'country','saves']

class SimpleUserSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    liked = LikeSerializer(many=True, read_only=True)
    commented=CommentSerializer(many=True, read_only=True)
    saved = SaveSerializer(many=True, read_only=True)
    reported = ReportSerializer(many=True, read_only=True)
    class Meta:
        model = SimpleUser
        fields = ['user', 'first_name', 'last_name','Dialogs','gender','email','phone_number', 'birthday', 'photo', 'city', 'country', 'street', 'postal_code', 'posts','commented','liked','saved','reported']

class SimpleUserUserCreateSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(required=True, write_only=True)
    phone_number = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = SimpleUser
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number',  'password']

    def create(self, validated_data):
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        email = validated_data.get('email')
        password = validated_data.pop('password')
        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,password=password)
        user.save()
        simpleuser = SimpleUser.objects.create(user=user, **validated_data)
        simpleuser.save()
        return simpleuser



class DialogSerializer(serializers.ModelSerializer):
    msgs = MessageSerializer(many=True, read_only=True)
    user1_name = serializers.ReadOnlyField(source='user1.get_full_name')
    user2_name = serializers.ReadOnlyField(source='user2.get_full_name')
    class Meta:
        model = Dialog
        fields = ['users','user1_name','user1','user2','user2_name','msgs','id','created_date']
    
    