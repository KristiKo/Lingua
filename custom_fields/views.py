from django.shortcuts import render
from .models import HowToApply, Faqs, PrivacyPolicy

def how_to_apply(request):
    fields = HowToApply.objects.all()
    context = {
        'fields': fields
        }
    return render(request, 'custom_fields/apply.html', context)
    

def faqs(request):
    fields = Faqs.objects.all()
    context = {
        'fields': fields
    }
    return render(request, 'custom_fields/faqs.html', context)


def privacy_policy(request):
    fields = PrivacyPolicy.objects.all()
    context = {
        'fields': fields
    }
    return render(request, 'custom_fields/privacy_policy.html', context)