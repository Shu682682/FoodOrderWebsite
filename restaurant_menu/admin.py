from django.contrib import admin
from .models import Item
class MenuItemAdmin(admin.ModelAdmin):
    list_display=("meal","status")#db field
    list_filter=("status",)#make sure add coma
    search_fields=("meal","description")
    
admin.site.register(Item,MenuItemAdmin)

#create user: python manage.py createsuperuser
#admin:admin/ pwd:whyneedpwd
#admin: admin@admin.com