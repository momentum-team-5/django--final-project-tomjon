from django.db import models
from django.contrib.auth.models import User

# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model

class Answer(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE)

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(User, related_name="favorites")