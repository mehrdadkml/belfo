from sqlite3 import Timestamp
from django.contrib import admin

from .models import Profile,Address

admin.site.register(Profile)
admin.site.register(Address)

# Register your models here.

