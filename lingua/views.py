from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from lingua.forms import ContactForm, SubscriberForm
from django.core.mail import send_mail, BadHeaderError
from .models import University, Programme, Course
from .filters import ProgrammeFilter, CourseFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from . import filters


def index(request):
    return render(request, 'lingua_templates/home.html')

def search_programme(request):
    programs_list = Programme.objects.all()
    programs_filter = ProgrammeFilter(request.GET, queryset=programs_list)
    filtered_qs = filters.ProgrammeFilter(
                      request.GET, 
                      queryset=Programme.objects.all()
                  ).qs
    paginator = Paginator(filtered_qs, 20)

    page = request.GET.get('page')
    try:
        programs = paginator.page(page)
    except PageNotAnInteger:
        programs = paginator.page(1)
    except EmptyPage:
        programs = paginator.page(paginator.num_pages)

    return render(
        request, 
        'lingua_templates/search/search_form_programme.html', 
        {'programs': programs, 'filter': programs_filter}
    )

def search_course(request):
    course_list = Course.objects.all()
    course_filter = CourseFilter(request.GET, queryset=course_list)
    filtered_qs = filters.CourseFilter(
                    request.GET,
                    queryset = Course.objects.all()
                ).qs
    paginator = Paginator(filtered_qs, 20)
    page = request.GET.get('page')
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)

    return render(
        request, 
        'lingua_templates/search/search_form_course.html', 
        {'courses':courses, 'filter': course_filter}
    )

def subscribe(request):
    score = 0
    if request.method == 'GET':
        form = SubscriberForm()
    else:
        form = SubscriberForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            question = form.cleaned_data['question']
            if question == 'teeth':
                score = 100
            form.save()
            messages.success(request, f'Your have successfully subscribed to our weekly newsletter. Your score is: ' + str(score))
            return redirect('index')
    return render(request, "lingua_templates/subscribe.html", {'form':form}) 

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            phone_number = form.cleaned_data['phone_number']
            day = form.cleaned_data['day']
            time = form.cleaned_data['time']
            message = form.cleaned_data['message']
            message = message + '. Callback requested from number: ' + phone_number + ' on this day: ' + day + ' at this time: ' + time
            try:
                send_mail(subject, message, from_email, ['hello@linguainternational.org'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "lingua_templates/contact.html", {'form': form})

def thanks(request):
    return HttpResponse('Thank you for your message.')
