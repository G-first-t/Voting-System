from django.contrib import admin
from .models import Question,Choice

# Register your models here.
admin.site.site_header="The Poll Mall"
admin.site.site_title="Voting Admin Area"
admin.site.index_title="Welcome To Our Voting Admin Area"