from .models import University, Programme, College, Course
from django import forms
import django_filters

class ProgrammeFilter(django_filters.FilterSet):
    university = django_filters.ModelChoiceFilter(queryset=University.objects.all())
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    city = django_filters.CharFilter(field_name='city', lookup_expr='icontains')
    award = django_filters.CharFilter(field_name='award', lookup_expr='icontains')
    max_cost = django_filters.NumberFilter(field_name='original_cost', lookup_expr='lte')
    min_cost = django_filters.NumberFilter(field_name='original_cost', lookup_expr='gte')

    class Meta:
        model = Programme
        fields = ['university', 'name', 'city', 'award', 'max_cost', 'min_cost']


class CourseFilter(django_filters.FilterSet):
    college = django_filters.ModelChoiceFilter(queryset=College.objects.all())
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    city = django_filters.CharFilter(field_name='city', lookup_expr='icontains')
    max_cost = django_filters.NumberFilter(field_name='original_cost1', lookup_expr='lte')
    min_cost = django_filters.NumberFilter(field_name='original_cost1', lookup_expr='gte')
    housing = django_filters.BooleanFilter()
    

    class Meta:
        model = Course
        fields = ['college', 'name', 'city', 'max_cost', 'min_cost', 'housing']