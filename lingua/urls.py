from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from lingua.models import Programme, Course, ProgrammeTestimonial, CourseTestimonial
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search_programme/$', views.search_programme, name='search_programme'),
    url(r'^search_programme/$', ListView.as_view(queryset=Programme.objects.all()[:25],
                                        template_name="lingua_templates/home.html")),
    url(r'^search_programme/(?P<pk>\d+)/$', DetailView.as_view(model=Programme,
                                        template_name = 'lingua_templates/single_programme.html')),
    url(r'^search_programme/(?P<pk>\d+)/$', DetailView.as_view(model=ProgrammeTestimonial,
                                        template_name = 'lingua_templates/testimonials/single_testimonial_programme.html')),
    url(r'^search_course/$', views.search_course, name='search_course'),
    url(r'^search_course/$', ListView.as_view(queryset=Course.objects.all()[:25],
                                        template_name="lingua_templates/home.html")),
    url(r'^search_course/(?P<pk>\d+)/$', DetailView.as_view(model=Course,
                                        template_name = 'lingua_templates/single_course.html')),
    url(r'^search_course/(?P<pk>\d+)/$', DetailView.as_view(model=CourseTestimonial,
                                        template_name = 'lingua_templates/testimonials/single_testimonial_course.html')),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^thank-you-for-reaching-us/$', views.thanks, name='thanks'),
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: ", content_type="text/plain"))
]