from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "vehicle_type",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("vehicle_type",)}),)
    #add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("vehicle_type",)}),)
    # Override add_fieldsets to avoid issues with non-existent fields 
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            #'fields': ('username', 'password1', 'password2', 'vehicle_type')}
            'fields': ('username', 'email', 'password1', 'password2', 'vehicle_type', 'is_staff')}
        ),
    )
    # https://forum.djangoproject.com/t/when-i-add-new-user-from-admin-panel-this-error-help/35124/8
    
admin.site.register(CustomUser, CustomUserAdmin)