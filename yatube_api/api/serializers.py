from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserGeo, Country, City

from posts.models import Post, Comment, Group, Follow

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')

    def validate_following(self, value):
        user = self.context['request'].user
        if user == value:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя'
            )
        return value

    def validate(self, attrs):
        user = self.context['request'].user
        following = attrs.get('following')

        if Follow.objects.filter(user=user, following=following).exists():
            raise serializers.ValidationError(
                'Вы уже подписаны на этого пользователя'
            )
        return attrs

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')


class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = City
        fields = ('id', 'name', 'country')


class UserGeoSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    city = CitySerializer(read_only=True)

    class Meta:
        model = UserGeo
        fields = ('country', 'city')


class UserSerializer(serializers.ModelSerializer):
    geo = UserGeoSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'geo')