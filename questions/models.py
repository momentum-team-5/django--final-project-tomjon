from django.db import models
from django.conf import settings

class Question(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='questions')
    favorites = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='favorites')

    def numfavorites(self):
        return self.favorites.count() 

    def correct_answers(self):
        return self.answers.filter(correct_answer = True)       

class Answer(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='answers')
    answer_favorites = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='answer_favorites')
    correct_answer = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='answers')


    def numfavorites(self):
        return self.answer_favorites.count()