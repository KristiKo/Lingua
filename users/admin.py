from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, Subscriber

# Extends the admin panel showing the User profile data
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

class SubscribersAdmin(admin.ModelAdmin):
    model = Subscriber


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Subscriber, SubscribersAdmin)