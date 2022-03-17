from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

#unregister the provided model admin
admin.site.unregister(User)


#register out own model admin, based on the default UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):

    actions = ['update', 'destroy',]


