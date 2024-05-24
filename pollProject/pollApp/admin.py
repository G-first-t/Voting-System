from django.contrib import admin

# Register your models here.
class PollAppAdmin(admin.AdminSite):
    site_title="The Voting System"
    set_header="The Poll Mall"
    index_title="The Voting System"

admin_site=PollAppAdmin(name="pollApp")

