
from django.db import models
from django.db.models import *
from django.urls import reverse
from backend.users.models import User
from django.contrib.auth.hashers import make_password
from django.db import models
from django.db.models import Model
from django.db.models.options import Options 
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.functions import datetime
from django.db.models import Avg, Sum
import datetime
from model_utils.models import TimeStampedModel
from django.utils import timezone

class Address(models.Model):
    city = models.CharField(verbose_name='City', max_length=255, null=True, blank=False)
    country = models.CharField(verbose_name='Country', max_length=255, null=True, blank=False)
    street = models.CharField(verbose_name='Street', max_length=255, null=True, blank=False)
    postal_code = models.PositiveIntegerField(verbose_name='Postal code', null=True, blank=False)
    
    class Meta:
        abstract = True 

    
class Personal(Address):
    MALE = 'Male'
    FEMALE ='Female'
    GENDER_CHOICES =  [
        (MALE, 'Male'), 
        (FEMALE, 'Female')
    ]

    first_name = models.CharField(verbose_name='First name', max_length=255, null=False, blank=False)
    last_name = models.CharField(verbose_name='Last name', max_length=255, null=False, blank=False)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    email = models.EmailField(verbose_name='Email', null=False, unique=True)
    phone_number = models.CharField(verbose_name='Phone number', max_length=255, 
                                            null=False, blank=True, unique=True)
    birthday = models.DateField(verbose_name='Birthday', null=True, blank=True)
    photo = models.ImageField(verbose_name='Photo', upload_to='images/', null=True,blank=True,default='download.jpeg')  
    
    
    class Meta :
        abstract = True

class SimpleUser(Personal):  
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True, null=False)
    
    @property
    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    @property
    def get_full_address(self):
         return "%s %s" % (self.city, self.country, self.street, self.postal_code)
    
class Post(Address):
    LOST = 'Lost'
    FOUND ='Found'
    DONATION ='Donation'
    PERSON = 'Person'
    OTHER='Other'
    MONEY='Money'
    CAR="Car"
    PET="Pet"
    DOC="Document"
    PHONE="Phone"
    KIND_CHOICES =  [
        (LOST, 'Lost'), 
        (FOUND, 'Found'),
        (DONATION, 'Donation')
    ]
    CAT_CHOICES =  [
        (PERSON , 'Person'), 
        (MONEY, 'Money'),
        (DOC,'Document'),
        (PHONE,'Phone'),
        (PET,'Pet'),
        (CAR,'Car'),
        (OTHER,'Other')
    ]
    id = models.AutoField(primary_key=True)
    date_create = models.DateTimeField(verbose_name='Created date', null=True, blank=True)
  #  likes = models.ManyToManyField(SimpleUser,verbose_name='Likes',related_name='liked', null=True, blank=True)
   # dislikes = models.ManyToManyField(SimpleUser,verbose_name='Dislikes',related_name='disliked', null=True, blank=True)
   #shares =  models.ManyToManyField(SimpleUser,verbose_name='Shares',related_name='shared', null=True, blank=True)
   # saves= models.ManyToManyField(SimpleUser,verbose_name='Saves',related_name='saved', null=True, blank=True)
    about = models.CharField(verbose_name='About', max_length=255, null=True, blank=False)
    image = models.ImageField(verbose_name='Image', upload_to='images/', null=True,blank=True)  
    kind = models.CharField(max_length=10, choices=KIND_CHOICES, null=True, blank=True)
    category = models.CharField(max_length=16, choices=CAT_CHOICES, null=True, blank=True)
    publisher = models.ForeignKey(SimpleUser, related_name='posts', on_delete=models.CASCADE, null=True)

    

class Like(models.Model):
    id = models.AutoField(primary_key=True)
    liker = models.ForeignKey(SimpleUser, related_name='liked', on_delete=models.CASCADE, null=True)
    postID= models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE, null=True)
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    auther = models.ForeignKey(SimpleUser, related_name='commented', on_delete=models.CASCADE, null=True)
    postID= models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, null=True)
    content = models.CharField(verbose_name='Comment', max_length=255, null=True, blank=False)
    created_date = models.DateTimeField( null=True, blank=True)
class SavePost(models.Model):
    id = models.AutoField(primary_key=True)
    savedby = models.ForeignKey(SimpleUser, related_name='saved', on_delete=models.CASCADE, null=True)
    postID= models.ForeignKey(Post, related_name='saves', on_delete=models.CASCADE, null=True)
class ReportPost(models.Model):
    id = models.AutoField(primary_key=True)
    reportedby = models.ForeignKey(SimpleUser, related_name='reported', on_delete=models.CASCADE, null=True)
    postID= models.ForeignKey(Post, related_name='reports', on_delete=models.CASCADE, null=True)

class Conversation(models.Model):

    users = models.ManyToManyField(SimpleUser,related_name='Dialogs',max_length=3)
    user1=models.ForeignKey(SimpleUser, related_name='send_rcv', on_delete=models.CASCADE, null=True)
    user2=models.ForeignKey(SimpleUser, related_name='rcv_send', on_delete=models.CASCADE, null=True)
    id=models.PositiveIntegerField(primary_key=True)
    created_date = models.DateTimeField( null=True, blank=True)
    class Meta:
        abstract = True
class Dialog(Conversation):
    pass

   
# 
# 
# 
# 
# 
# 

class Message(models.Model):
    id=models.AutoField(primary_key=True)
    dialog=models.ForeignKey(Dialog,related_name='msgs',on_delete=models.CASCADE,null=True,blank=True)
    content = models.TextField()
    sender = models.ForeignKey(SimpleUser, related_name="sends",on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)
    sent_at = models.DateTimeField(null=True, blank=True)

   

    @property


    def __str__(self):
        return self.content

    def save(self, **kwargs):
        if not self.id:
            self.sent_at = timezone.now()
        super(Message, self).save(**kwargs)

