from django.db import models
from datetime import datetime, timedelta, date
from django.contrib.auth.models import User

# Create your models here.

class Autor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    rating = models.IntegerField()
    autor = models.OneToOneField(Autor, on_delete=models.CASCADE)
    likes = Likes.objects.filter(attitude=True)
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return '/question/%d/' % self.qn
    class Meta:
        db_table = 'qa_question'
        ordering = ['-added_at']

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    question = models.OneToOneField(Question)
    autor = models.OneToOneField(Autor, on_delete=models.CASCADE)
    class Meta:
        db_table = 'qa_answer'
        ordering = ['-added_at']

class Likes(models.Model):
    user = models.ForeignKey(Autor)
    question = models.ForeignKey(Question)
    attitude = models.BooleanField()

class QuestionManager(models.Manager):
    def get_new(self):
        newest = []
        begin = datetime.date.today() - timedelta(days=2)
        for q in Question.objects.filter(added_at__gte=begin):
            newest.append(q)
        return newest
    
    def get_popular(self):
        popular = []
        for q in Question.objects.order_by('-rating'):
            popular.append(q)
        return popular
        

