from .models import University, Programme, College, Course
from django import forms
import django_filters

class ProgrammeFilter(django_filters.FilterSet):
    university = django_filters.ModelChoiceFilter(queryset=University.objects.all())
    name = django_filters.CharFilter(lookup_expr='icontains')
    cost = django_filters.NumberFilter(field_name='original_cost', lookup_expr='lt') # 'gt' for min range value 'lt' for max range value
    

    class Meta:
        model = Programme
        fields = ['university', 'name', 'cost']


class CourseFilter(django_filters.FilterSet):
    college = django_filters.ModelChoiceFilter(queryset=College.objects.all())
    name = django_filters.CharFilter(lookup_expr='icontains')
    cost = django_filters.NumberFilter(field_name='original_cost1', lookup_expr='lt')
    

    class Meta:
        model = Course
        fields = ['college', 'name', 'cost']