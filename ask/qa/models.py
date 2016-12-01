from django.db import models
from datetime import datetime, timedelta, date, time
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.

class QuestionManager(models.Manager):
    def new(self):
         return self.order_by('-added_at')
    
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255, default='', null=True, blank=True)
    text = models.TextField(default='', null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True, auto_now=True, null=True, blank=True)
    rating = models.IntegerField(default=0, null=True)
    author = models.ForeignKey(User, null=True, default=None)
    likes = models.ManyToManyField(User, related_name='user_likes_question', null=True)
    
    def __unicode__(self):
        return self.title

    def get_url(self):
        return reverse('question', kwargs = {'qn': self.pk})

    class Meta:
        db_table="qa_question"
        ordering=['-added_at']

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, null=True, default=None, blank=True)
    
    class Meta:
        db_table="qa_answer"
        ordering=['-added_at']

class Test():
    for i in range(0):
        Question.objects.create(title = "How to run Hello World?",
                                text = """
                                How many variants do you know to write Hello
                                World in Python 2.7.13? """,
                                added_at = "2016-11-29",
                                rating = 0,
                                author = User.objects.get(id=1))
    for i in xrange(0):
        for j in xrange(0):
            Answer.objects.create(text = """
                                  You can google this question on your
                                  fucking computer idiot. """,
                                  added_at="2016-11-29",
                                  question=Question.objects.get(id=i),
                                  author=User.objects.get(id=1))
