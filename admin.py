from django.contrib import admin
from .models import Rating, post
admin.site.register(post)
admin.site.register(Rating)

