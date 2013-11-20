from django.contrib import admin
from books.models import Publisher,Author,Student,Book
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
    search_fields = ('first_name','last_name')
class StudentAdmin(admin.ModelAdmin):
    list_display=('name','address','city')
    search_fields =('name','address')
admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
#admin.site.register(Author)
admin.site.register(Student,StudentAdmin)
admin.site.register(Book)
