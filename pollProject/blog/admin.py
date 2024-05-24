# blog/admin.py
from django.contrib import admin
from .models import Post

class AdminArea(admin.AdminSite):
    site_title = "The Boss site"
    index_title = "Site for editing"
    site_header = "Admin Dashboard"

blog_site = AdminArea(name="BlogAdmin")
blog_site.register(Post)
