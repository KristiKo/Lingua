# Generated by Django 2.1.7 on 2019-03-07 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lingua', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursetestimonial',
            name='reviews_link',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='programmetestimonial',
            name='reviews_link',
            field=models.URLField(null=True),
        ),
    ]
