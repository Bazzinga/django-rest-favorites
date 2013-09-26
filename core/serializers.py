from django.forms import widgets
from django.contrib.auth.models import User

from rest_framework import serializers

from core.models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):

    owner = serializers.Field(source='owner.username')

    class Meta:
        model = Favorite
        fields = ('content', 'description', 'owner', 'created')


class UserSerializer(serializers.ModelSerializer):
    favorites = FavoriteSerializer(many=True, view_name='favorite-detail')

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'favorites')