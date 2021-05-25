from rest_framework import serializers

from .models import Api, User, Review

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')


class ApiSerializer(serializers.ModelSerializer):
    liked_by = UserSerializer(read_only=True)

    class Meta:
        model = Api
        fields = ('id', 'brand', 'name', 'release_year', 'release_date', 'liked_by')

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'review')