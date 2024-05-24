from django.contrib import admin
from .models import Question,Choice

# Register your models here.
class PollAppAdmin(admin.AdminSite):
    site_title="The Voting System"
    site_header="The Poll Mall"
    index_title="The Voting System"

admin_site=PollAppAdmin(name="pollApp")

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=4

class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[
        
            ('section_1',{'fields':['question_text']}),
            ('section_2',{'fields':['pub_date'],'classes':['collapse']}),
        
    ]
    inlines=[ChoiceInline]

admin_site.register(Question,QuestionAdmin)