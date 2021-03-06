from django.db import models

class University(models.Model):
    name = models.CharField(max_length=140)
    city = models.CharField(max_length=140)
    university_url = models.URLField(null=True)

    def __str__(self):
        return self.name


class Programme(models.Model):
    university = models.ForeignKey('lingua.University', on_delete=models.CASCADE, related_name='universities')
    image = models.ImageField(default='LinguaLogo.jpg', upload_to='university_img')
    name = models.CharField(max_length=140, null=True)
    address_link = models.URLField(null=True)
    address = models.CharField(max_length=140, null=True)
    coordinate_lat = models.DecimalField(max_digits=7, decimal_places=4, null=True)
    coordinate_long = models.DecimalField(max_digits=7, decimal_places=4, null=True)
    programme_url = models.URLField(null=True)
    duration = models.IntegerField(null=True)
    ranking = models.CharField(max_length=140, null=True)
    start_date = models.DateField(null=True)
    award = models.CharField(max_length=140, null=True)
    level = models.CharField(max_length=140, null=True)
    description = models.TextField(null=True)
    attendance = models.CharField(max_length=140, null=True)
    learning_mode = models.CharField(max_length=140, null=True)
    original_cost = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    discount_cost = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name



class College(models.Model):
    name = models.CharField(max_length=140)
    city = models.CharField(max_length=140)
    college_url = models.URLField(null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    college = models.ForeignKey('lingua.College', on_delete=models.CASCADE, related_name='colleges')
    image = models.ImageField(default='LinguaLogo.jpg', upload_to='college_img')
    name = models.CharField(max_length=140, null=True)
    address_link = models.URLField(null=True)
    address = models.CharField(max_length=140, null=True)
    coordinate_lat = models.DecimalField(max_digits=7, decimal_places=4, null=True)
    coordinate_long = models.DecimalField(max_digits=7, decimal_places=4, null=True)
    college_url = models.URLField(null=True)
    duration = models.IntegerField(null=True)
    start_date = models.CharField(max_length=140, null=True, blank=True)
    type = models.CharField(max_length=140, null=True)
    description = models.TextField(null=True)
    attendance = models.CharField(max_length=140, null=True)
    learning_mode = models.CharField(max_length=140, null=True)
    student_per_class = models.IntegerField(null=True)
    lesson_durations = models.IntegerField(null=True)
    option1 = models.CharField(max_length=140, null=True, blank=True)
    original_cost1 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    discount_cost1 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    option2 = models.CharField(max_length=140, null=True, blank=True)
    original_cost2 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    discount_cost2 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    option3 = models.CharField(max_length=140, null=True, blank=True)
    original_cost3 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    discount_cost3 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    option4 = models.CharField(max_length=140, null=True, blank=True)
    original_cost4 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    discount_cost4 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    option5 = models.CharField(max_length=140, null=True, blank=True)
    original_cost5 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    discount_cost5 = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    housing = models.BooleanField(null=True)
    housing_description = models.TextField(null=True, blank=True)
    min_age = models.IntegerField(null=True)
    distance = models.CharField(max_length=140, null=True)
    meals = models.CharField(max_length=140, null=True)
    housing_cost = models.DecimalField(max_digits=7, decimal_places=2, null=True)


    def __str__(self):
        return self.name


class ProgrammeTestimonial(models.Model):
    programme = models.ForeignKey('lingua.Programme', on_delete=models.CASCADE, related_name='programmes')
    name = models.CharField(max_length=140, null=True)
    picture = models.ImageField(default='default.jpg', upload_to='programme_testimonials')
    comment = models.TextField(null=True)
    rating = models.CharField(max_length=140, null=True)

    def __str__(self):
        return self.name

class CourseTestimonial(models.Model):
    programme = models.ForeignKey('lingua.Course', on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=140, null=True)
    picture = models.ImageField(default='default.jpg', upload_to='programme_testimonials')
    comment = models.TextField(null=True)
    rating = models.CharField(max_length=140, null=True)

    def __str__(self):
        return self.name

class GeneralTestimonial(models.Model):
    name = models.CharField(max_length=140, null=True)
    picture = models.ImageField(default='default.jpg', upload_to='programme_testimonials')
    comment = models.TextField(null=True)
    rating = models.CharField(max_length=140, null=True)

    def __str__(self):
        return self.name
