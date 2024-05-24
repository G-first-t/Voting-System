
from django.contrib import admin
from django.urls import path
from blog.admin import blog_site

urlpatterns = [
    path('admin/', blog_site.urls),
]


