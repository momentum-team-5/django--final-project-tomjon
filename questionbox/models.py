from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(User, related_name='favorite')

    @property
    def answers(self):
        return Answer.objects.filter(question=self)

    def numfavorites(self):
        return self.favorites.all().count()    

class Answer(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    question = models.ForeignKey('Question', on_delete=models.CASCADE)