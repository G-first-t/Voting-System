from django.contrib import admin


# Register your models here.
class AdminArea(admin.AdminSite):
    site_title="The Boss site"
    index_title="site for editing"
    site_header="admin dashboard"


blog_site=AdminArea(name="BlogAdmin")