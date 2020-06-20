from django.db import models
from django.contrib.auth.models import User
#from django.utils import timezone
import datetime
from django.urls import reverse
# Create your models here.
class Question(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)  #user who is logged in
    title=models.CharField(max_length=200) # title of qestion
    question=models.TextField() #question
    created_time= models.DateTimeField(default=datetime.datetime.now()) #question creation time
    answer_count=models.IntegerField(default=0) #total reply or answer count
    qustion_upvote=models.IntegerField(default=0) #question upvote
    question_downvote=models.IntegerField(default=0) #question q

    def __str__(self):
        return self.question


    def get_absolute_url(self):
        return reverse('home')


class Answer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE) #user who logged in
    selected_question=models.ForeignKey(Question,on_delete=models.CASCADE) #selected question for which we wants to answer
    answer=models.TextField() #answer for question
    answer_created_time=models.DateTimeField(default=datetime.datetime.now()) #time when user answered the question
    answer_upvote=models.IntegerField(default=0) #answer upvote
    answer_downvote=models.IntegerField(default=0) #answer downvote

    def __str__(self):
        return self.answer


    def get_absolute_url(self):
        return reverse('question-detail',kwargs={'pk':self.selected_question.id})
