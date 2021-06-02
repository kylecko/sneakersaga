from rest_framework import serializers

from .models import Sneaker, User, Review

class UserSerializer(serializers.ModelSerializer):
    # need to keep password from going out

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')


class SneakerSerializer(serializers.ModelSerializer):
    #liked_by = UserSerializer(read_only=True)

    class Meta:
        model = Sneaker
        fields = ('id', 'brand', 'name', 'release_year', 'desc', 'img', 'review')

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'review', 'creator', 'sneaker_review')