from django.contrib import admin
from rango.models import Category, Page, UserProfile
# Register your models here.

admin.site.register(Category)
admin.site.register(UserProfile)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category','url')
    
admin.site.register(Page, PageAdmin)