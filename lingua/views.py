from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from lingua.forms import ContactForm, SubscriberForm
from django.core.mail import send_mail, BadHeaderError
from .models import University, Programme, Course
from .filters import ProgrammeFilter, CourseFilter
import datetime

def index(request):
    return render(request, 'lingua_templates/home.html')

def search_programme(request):
    programme_list = Programme.objects.all()
    programme_filter = ProgrammeFilter(request.GET, queryset=programme_list)
    return render(request, 'lingua_templates/search/search_form_programme.html', {'filter': programme_filter})

def search_course(request):
    course_list = Course.objects.all()
    course_filter = CourseFilter(request.GET, queryset=course_list)
    return render(request, 'lingua_templates/search/search_form_course.html', {'filter': course_filter})

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
