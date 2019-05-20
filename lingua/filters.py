from .models import University, Programme, College, Course
from django import forms
import django_filters

class ProgrammeFilter(django_filters.FilterSet):
    university = django_filters.ModelChoiceFilter(queryset=University.objects.all())
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    university__city = django_filters.CharFilter(lookup_expr='icontains')
    award = django_filters.CharFilter(field_name='award', lookup_expr='icontains')
    max_cost = django_filters.NumberFilter(field_name='original_cost', lookup_expr='lte')
    min_cost = django_filters.NumberFilter(field_name='original_cost', lookup_expr='gte')

    class Meta:
        model = Programme
        fields = ['university', 'name', 'university__city', 'award', 'max_cost', 'min_cost']


class CourseFilter(django_filters.FilterSet):
    college = django_filters.ModelChoiceFilter(queryset=College.objects.all())
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    college__city = django_filters.CharFilter(lookup_expr='icontains')
    max_cost = django_filters.NumberFilter(field_name='original_cost1', lookup_expr='lte')
    min_cost = django_filters.NumberFilter(field_name='original_cost1', lookup_expr='gte')
    housing = django_filters.BooleanFilter()
    

    class Meta:
        model = Course
        fields = ['college', 'name', 'college__city', 'max_cost', 'min_cost', 'housing']