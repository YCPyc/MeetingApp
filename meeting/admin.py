from django.contrib import admin
from .models import Post
# Register your models here.

# Initiate Post objects in admin page
admin.site.register(Post)