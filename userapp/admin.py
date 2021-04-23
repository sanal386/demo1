from django.contrib import admin
from .models import tbl_login, tbl_registration

class tbl_loginAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

class tbl_registrationAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','email','username','password','confirmpassword')    

# Register your models here.
admin.site.register(tbl_login, tbl_loginAdmin)
admin.site.register(tbl_registration, tbl_registrationAdmin)
