from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Own manager for models Question
class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')	
# Model Question
class Question(models.Model):
    # fields
    title = models.CharField(max_length = 255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add = True)
    rating = models.IntegerField(default = 0)
    objects = QuestionManager()
    # links
    author = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name = 'likes')
    # methods
    def get_url(self):
        return reverse('question', kwargs = {'id': self.id})
    def __unicode__(self) :
        return self.title

# Model Answer
class Answer(models.Model):
    # fields
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add = True)
    # links
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    author = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
