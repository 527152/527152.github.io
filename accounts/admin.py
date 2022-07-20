from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account




class AccountAdmin(UserAdmin): #editar el formato de la tabla de accounts en Django Administration
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_link = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


# Register your models here.
admin.site.register(Account, AccountAdmin ) #registrar la clase Account como parte de modelo
