# Generated by Django 3.1.2 on 2020-10-27 01:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0003_answer_answer_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_favorites',
            field=models.ManyToManyField(related_name='answer_favorites', to=settings.AUTH_USER_MODEL),
        ),
    ]
