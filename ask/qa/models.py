from django.db import models
from datetime import datetime, timedelta, date, time
from django.contrib.auth.models import User

# Create your models here.

class QuestionManager(models.Manager):
    def new(self):
         return self.order_by('-added_at')
    
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255, default='')
    text = models.TextField(default='')
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='user_likes_question')
    
    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/question/%d/' % self.pk

    class Meta:
        db_table="qa_question"
        ordering=['-added_at']

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
    
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
