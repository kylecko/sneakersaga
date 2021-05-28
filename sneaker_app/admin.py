from django.contrib import admin

from .models import User, Sneaker, Review

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Sneaker)
class SneakerAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

# Register your models here.
