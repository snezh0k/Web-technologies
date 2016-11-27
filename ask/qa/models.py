from django.db import models
from datetime import datetime, timedelta, date
from django.contrib.auth.models import User

# Create your models here.

class QuestionManager(models.Manager):
    def new(self):
        newest = []
        begin = datetime.date.today() - timedelta(days=2)
        for q in Question.objects.filter(added_at__gte=begin):
            newest.append(q)
        return newest
    
    def popular(self):
        popular = []
        for q in Question.objects.order_by('-rating'):
            popular.append(q)
        return popular

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
        return '/question/%d/' % self.qn

    class Meta:
        db_table="qa_question"
        ordering=['-added_at']

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.OneToOneField(Question)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table="qa_answer"
        ordering=['-added_at']
