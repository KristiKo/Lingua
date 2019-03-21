from .models import University, Programme, College, Course
from django import forms
import django_filters

class ProgrammeFilter(django_filters.FilterSet):
    university = django_filters.ModelChoiceFilter(queryset=University.objects.all())
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    city = django_filters.ModelChoiceFilter(queryset=University.objects.all().values_list('city', flat=True))
    award = django_filters.CharFilter(field_name='award', lookup_expr='icontains')
    max_cost = django_filters.NumberFilter(field_name='original_cost', lookup_expr='lt')
    min_cost = django_filters.NumberFilter(field_name='original_cost', lookup_expr='gt')

    class Meta:
        model = Programme
        fields = ['university', 'name', 'city', 'award', 'max_cost', 'min_cost']


class CourseFilter(django_filters.FilterSet):
    college = django_filters.ModelChoiceFilter(queryset=College.objects.all())
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    city = django_filters.ModelChoiceFilter(queryset=College.objects.all().values_list('city', flat=True))
    max_cost = django_filters.NumberFilter(field_name='original_cost1', lookup_expr='lt')
    min_cost = django_filters.NumberFilter(field_name='original_cost1', lookup_expr='gt')
    housing = django_filters.BooleanFilter()
    

    class Meta:
        model = Course
        fields = ['college', 'name', 'city', 'max_cost', 'min_cost', 'housing']