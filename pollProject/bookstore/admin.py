from django.contrib import admin
from .models import Book
# Register your models here.
class BookstoreArea(admin.AdminSite):
    site_title="BookStore"
    index_site="books shelf"
    site_header="the bookstores"

    
book_site=BookstoreArea(name="books")

book_site.register(Book)


