from django.contrib import admin

# Register your models here.
from app1.models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','gendor')
    pass
admin.site.register(Author, AuthorAdmin)

admin.site.register(Publisher)
#admin.site.register(Author)
admin.site.register(Book)