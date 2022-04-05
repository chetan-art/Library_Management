from django.contrib import admin
from .models import Add_Book_detail
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['Name','Author_Name','Publish_date','Price']

admin.site.register(Add_Book_detail,BookAdmin)