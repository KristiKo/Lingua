from django.contrib import admin
from lingua.models import University, Programme, College, Course, ProgrammeTestimonial, CourseTestimonial, GeneralTestimonial 


class UniversityAdmin(admin.ModelAdmin):
    model = University

class ProgrammeAdmin(admin.ModelAdmin):
    model = Programme

class CollegeAdmin(admin.ModelAdmin):
    model = College

class CourseAdmin(admin.ModelAdmin):
    model = Course

class ProgrammeTestimonialAdmin(admin.ModelAdmin):
    model = ProgrammeTestimonial

class CourseTestimonialAdmin(admin.ModelAdmin):
    model = CourseTestimonial

class GeneralTestimonialAdmin(admin.ModelAdmin):
    model = GeneralTestimonial

admin.site.register(University, UniversityAdmin)
admin.site.register(Programme, ProgrammeAdmin)
admin.site.register(College, CollegeAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(ProgrammeTestimonial, ProgrammeTestimonialAdmin)
admin.site.register(CourseTestimonial, CourseTestimonialAdmin)
admin.site.register(GeneralTestimonial, GeneralTestimonialAdmin)
