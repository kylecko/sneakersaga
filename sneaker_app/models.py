from django.db import models
import re
import bcrypt


class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at the minimum two characters!"

        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at the minimum two characters!"

        email_regex = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email!"
        elif not email_regex.match(postData['email']):
            errors['email'] = "Must be a valid email!"

        current_users = User.objects.filter(email=postData['email'])
        if len(current_users) > 0:
            errors['duplicate'] = "That email is already in use!"

        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least eight characters!"
        if postData['password'] != postData['confirm_password']:
            errors['mismatch'] = "Passwords don't match!"

        return errors

    def login_validator(self, postData):
        errors = {}
        existing_user = User.objects.filter(email=postData['email'])
        if len(existing_user) != 1:
            errors['email'] = "User does not exist!"
        if len(postData['email']) == 0:
            errors['email'] = "Email must be entered!"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least eight characters!"
        elif bcrypt.checkpw(postData['password'].encode(), existing_user[0].password.encode()) != True:
            errors['mismatch'] = "Email and password do not match!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Sneaker(models.Model):
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    release_year = models.DateField()
    desc = models.TextField(default="")
    liked_by = models.ManyToManyField(User, related_name="favorite_shoe", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    img = models.TextField(default=None, null=True)


    def __str__(self):
        return f'{self.brand} {self.name}'

class Review(models.Model):
    review = models.TextField()
    creator = models.ForeignKey(User, related_name="has_created_review", on_delete=models.CASCADE)
    sneaker_review = models.ForeignKey(Sneaker, related_name="shoe_review", on_delete=models.CASCADE)


# Create your models here.

