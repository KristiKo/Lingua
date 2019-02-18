from django.db import models
from froala_editor.fields import FroalaField

class HowToApply(models.Model):
    content = models.TextField(null=True)

    def __str__(self):
        return self.content

class Faqs(models.Model):
    question = models.CharField(max_length=140, null=True)
    answer = models.TextField(null=True)

    def __str__(self):
        return self.question

class PrivacyPolicy(models.Model):
    content = FroalaField(null=True)

    def __str__(self):
        return self.content
