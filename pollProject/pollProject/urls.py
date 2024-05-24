
from django.contrib import admin
from django.urls import path
from blog.admin import blog_site
from bookstore.admin import book_site

urlpatterns = [
    path('admin/',admin.site.urls),
    path('admin/', blog_site.urls),
    path('bookadmin/',book_site.urls)
]


