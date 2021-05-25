from django.contrib import admin

from .models import User, Api, Review

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Api)
class ApiAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

# Register your models here.
