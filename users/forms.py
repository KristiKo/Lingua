from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    name = forms.CharField(required=False)
    surname = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    phone = forms.CharField(required=False)
    street_address = forms.CharField(required=False)
    city = forms.CharField(required=False)
    zip_code = forms.CharField(required=False)
    passport = forms.ImageField(required=False)
    visa = forms.ImageField(required=False)
    cas = forms.FileField(required=False)
    recent_education = forms.FileField(required=False)
    university_preference = forms.CharField(required=False)
    course_preference = forms.CharField(required=False)
    english_level = forms.FileField(required=False)
    motivation_letter = forms.FileField(required=False)
    cv = forms.FileField(required=False)
    recommendation1 = forms.FileField(required=False)
    recommendation2 = forms.FileField(required=False)
    recommendation3 = forms.FileField(required=False)
    promo_code = forms.CharField(required=False)
    agree = forms.BooleanField(required=False)

    class Meta:
        model = Profile
        fields = ['image','name','surname','email','phone','street_address','city', 'zip_code', 'passport','visa','cas', 'recent_education', 'university_preference','course_preference','english_level','motivation_letter','cv','recommendation1','recommendation2','recommendation3', 'promo_code', 'agree']