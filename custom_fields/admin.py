from django.contrib import admin
from .models import HowToApply, Faqs, PrivacyPolicy
admin.site.site_header = 'Lingua International'

class HowToApplyAdmin(admin.ModelAdmin):
    model = HowToApply

class FaqsAdmin(admin.ModelAdmin):
    model = Faqs

class PrivacyPolicyAdmin(admin.ModelAdmin):
    model = PrivacyPolicy

admin.site.register(HowToApply, HowToApplyAdmin)
admin.site.register(Faqs, FaqsAdmin)
admin.site.register(PrivacyPolicy, PrivacyPolicyAdmin)