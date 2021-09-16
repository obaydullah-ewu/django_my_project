from django.contrib import admin

# Register your models here.
from App_Login.models import UserProfile

admin.site.register(UserProfile)