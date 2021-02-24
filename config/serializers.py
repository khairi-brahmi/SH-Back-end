
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from backend.app.models import SimpleUser
from backend.users.models import User

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        data.update({'user_id': self.user.id})
        data.update({'user_fname': self.user.first_name})
        data.update({'user_lname': self.user.last_name})
        return data 