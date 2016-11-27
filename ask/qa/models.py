from django.db import models
from datetime import datetime, timedelta, date
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='question_like_author', default='x')
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return '/question/%d/' % self.qn
    class Meta:
        db_table = 'qa_question'
        ordering = ['-added_at']

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.OneToOneField(Question)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'qa_answer'
        ordering = ['-added_at']

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
