from django.forms import widgets
from django.contrib.auth.models import User

from rest_framework import serializers

from core.models import Favorite


class FavoriteSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.Field(source='owner.username')

    class Meta:
        model = Favorite
        fields = ('url', 'content', 'description', 'owner', 'created')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    favorites = serializers.HyperlinkedRelatedField(many=True, view_name='favorite-detail')

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'favorites')