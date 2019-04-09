from django.db import models
from lingua.models import University, Programme, College, Course
from django.contrib.auth.models import User
from PIL import Image
from datetime import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    name = models.CharField(null=True, max_length=140)
    surname = models.CharField(null=True, max_length=140)
    email = models.EmailField(null=True, max_length=254)
    phone = models.CharField(null=True, max_length=140)
    street_address = models.CharField(null=True, max_length=140)
    city = models.CharField(null=True, max_length=140)
    zip_code = models.CharField(null=True, max_length=140)
    passport = models.ImageField(default='default_passport.jpg', upload_to='passports')
    visa = models.ImageField(default='default_visa.jpg', upload_to='visas')
    cas = models.FileField(null=True, upload_to="cas")
    university_preference = models.TextField(null=True)
    course_preference = models.TextField(null=True)
    english_level = models.FileField(null=True, upload_to='ielts')
    recent_education = models.FileField(null=True, upload_to='education')
    motivation_letter = models.FileField(null=True, upload_to='motivation_letters')
    cv = models.FileField(null=True, upload_to='cv')
    recommendation1 = models.FileField(null=True, upload_to='recommendations')
    recommendation2 = models.FileField(null=True, upload_to='recommendations')
    recommendation3 = models.FileField(null=True, upload_to='recommendations')
    agreement = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)