from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            nickname=validated_data['nickname'],
            real_name=validated_data['real_name'],
            password=validated_data['password']
        )
        return user

    class Meta:
        model = User
        fields = ['nickname', 'email', 'real_name', 'registration_date', 'birth_date',
                  'photo', 'stacks', 'homepage', 'blog', 'contact', 'description', 'feed_mail']
