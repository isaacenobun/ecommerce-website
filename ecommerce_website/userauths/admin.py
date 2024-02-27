import site
from django.contrib import admin
from .models import User

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email','bio','last_login')
    search_fields = ['username','email']

# Register your models here.
admin.site.register(User,CustomUserAdmin)