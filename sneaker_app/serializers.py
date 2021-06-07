from rest_framework import serializers

from .models import Sneaker, User, Review

class UserSerializer(serializers.ModelSerializer):
    # need to keep password from going out
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {
            'password': {}
        }

class ReviewSerializer(serializers.ModelSerializer):
    creator = UserSerializer()

    class Meta:
        model = Review
        fields = ('id', 'review', 'creator', 'sneaker_review')

class SneakerSerializer(serializers.ModelSerializer):
    #liked_by = UserSerializer(read_only=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Sneaker
        fields = ('id', 'brand', 'name', 'release_year', 'desc', 'img', 'reviews')


# server {
#   listen 80;
#   server_name 18.117.145.31;
#   location = /favicon.ico { access_log off; log_not_found off; }
#   location /static/ {
#       root /home/ubuntu/sneakersaga;
#   }
#   location / {
#       include proxy_params;
#       proxy_pass http://unix:/home/ubuntu/sneakersaga/sneaker_saga.sock;
#   }
# }

# [Unit]
# Description=gunicorn daemon
# After=network.target
# [Service]
# User=ubuntu
# Group=www-data
# WorkingDirectory=/home/ubuntu/sneakersaga
# ExecStart=/home/ubuntu/sneakersaga/venv/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/sneakersaga/sneaker_saga.sock sneaker_saga.wsgi:application
# [Install]
# WantedBy=multi-user.target