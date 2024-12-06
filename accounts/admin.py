from django.contrib import admin
from . models import Account
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    #it will make the password read only since it is not listed on the list display.
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    
    #show the date in decending order.
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    

# Register your models here.

admin.site.register(Account,AccountAdmin)
