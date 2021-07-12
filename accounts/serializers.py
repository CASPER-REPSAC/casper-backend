from .models import User
from rest_framework import serializers
from .models import Appeal, Activist, Observer, Rescuer


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


class AppealSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    class Meta:
        model = Appeal
        fields = ['url', 'id', 'author', 'updated_date', 'content']


class ActivistSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    class Meta:
        model = Activist
        fields = ['url', 'id', 'owner', 'visible', 'point', 'total_point']


class ObserverSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    class Meta:
        model = Observer
        fields = ['url', 'id', 'owner', 'visible', 'point', 'total_point']


class RescuerSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    class Meta:
        model = Rescuer
        fields = ['url', 'id', 'owner', 'visible', 'point', 'total_point']

