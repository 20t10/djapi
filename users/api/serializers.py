from rest_framework import serializers
from users.models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
class UserDisplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["username"]