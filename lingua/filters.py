from .models import University, Programme, College, Course
from django import forms
import django_filters

class UniversityFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    city = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = University
        fields = ['name', 'city', ]

class ProgrammeFilter(django_filters.FilterSet):
    university = django_filters.ModelChoiceFilter(queryset=University.objects.all())
    name = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.ModelMultipleChoiceFilter(queryset=Programme.objects.all(), widget=forms.CheckboxSelectMultiple)
    duration = django_filters.CharFilter(lookup_expr='icontains')
    start_date = django_filters.DateFilter()
    type = django_filters.CharFilter(lookup_expr='icontains')
    attendance = django_filters.CharFilter(lookup_expr='icontains')
    learning_mode = django_filters.CharFilter(lookup_expr='icontains')
    

    class Meta:
        model = Programme
        fields = ['university', 'name', 'price', 'duration', 'start_date', 'type', 'attendance', 'learning_mode']



class CollegeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    city = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = College
        fields = ['name', 'city', ]

class CourseFilter(django_filters.FilterSet):
    college = django_filters.ModelChoiceFilter(queryset=College.objects.all())
    name = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.ModelMultipleChoiceFilter(queryset=Course.objects.all(), widget=forms.CheckboxSelectMultiple)
    duration = django_filters.CharFilter(lookup_expr='icontains')
    start_date = django_filters.DateFilter()
    type = django_filters.CharFilter(lookup_expr='icontains')
    attendance = django_filters.CharFilter(lookup_expr='icontains')
    learning_mode = django_filters.CharFilter(lookup_expr='icontains')
    

    class Meta:
        model = Course
        fields = ['college', 'name', 'price', 'duration', 'start_date', 'type', 'attendance', 'learning_mode']