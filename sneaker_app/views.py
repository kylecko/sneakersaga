from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Sneaker, Review
import bcrypt

from rest_framework import viewsets, permissions, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User, Sneaker, Review
from .serializers import UserSerializer, SneakerSerializer, ReviewSerializer


def index(request):
    return render(request, 'index.html')


class UserViewset(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    permissions_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=False, methods=['POST'], url_path='register')
    def register(self, request, *args, **kwargs):
        try:  # sessions
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                # hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
                # request.session['logged_user'] = log_user.id
                user = serializer.save()
                request.session['logged_user'] = user.id
                # Encrypt the password
                return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            print(ex)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['POST'], url_path='login')
    def login(self, request, *args, **kwargs):
        try:  # sessions
            if request.method == "POST":
                
                users = User.objects.filter(email=request.data.get('email', None)).filter(password=request.data.get('password', None))
                
                if users.count() > 0:
                    log_user = users[0]
                    request.session['logged_user'] = log_user.id
            
                    return Response(UserSerializer(log_user).data, status=status.HTTP_200_OK)

        except Exception as ex:
            print(ex)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['POST'], url_path='logout')
    def logout(self, request):
        try:
            if request.method == "POST":
                request.session.flush()
            return Response(status=status.HTTP_200_OK)
        except Exception as ex:
            print(ex)

        return Response(status=status.HTTP_400_BAD_REQUEST)


    # clear session, returen 200


class SneakerViewset(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    permissions_classes = (permissions.AllowAny,)
    serializer_class = SneakerSerializer
    queryset = Sneaker.objects.all()

    # @action(detail=False, methods=['GET'], url_path='like_book/(?P<member_id>\d+)/(?P<book_id>\d+)')
    # def like_book(self, request, member_id ,book_id):

    #     try:
    #         book = Book.objects.get(id=book_id)
    #         member = Member.objects.get(id=member_id)

    #         if book in member.books_liked.all():
    #             member.books_liked.remove(book)
    #         else:
    #             member.books_liked.add(book)

    #         return Response(BookSerializer(book).data, status=status.HTTP_200_OK)

    #     except Exception as ex:
    #         pass

    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    # POST user ID, sneakerID, review
    def add_review():
        # create a review
        # return review with 200
        pass


class ReviewViewset(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    permissions_classes = (permissions.AllowAny,)
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

# Create your views here.
