from django.contrib import admin
from django.contrib.auth import get_user_model

# from backend.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()

admin.site.register(User)

