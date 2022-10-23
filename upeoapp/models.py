from django.db import models
# Create your models here

class Student(models.Model):
      first_name = models.CharField(max_length=15,null=True)
      last_name = models.CharField(max_length=15,null=True)
      admission_number = models.CharField(max_length=10,null=True)
      phone_number =
      
      #added notification model
      
class Notification(models.Model):
      status = models.CharField(max_length = 6,null=True)
      STATUS_CHOICE = (
        ('read','read'),
        ('unread','unread'),
    )

      message = models.CharField(max_length = 15,null=True)
      date = models.DateTimeField()
      origin = models.CharField(max_length = 6,null=True)
      destination = models.ForeignKey(to=Student,on_delete=models.CASCADE)
      title = models.CharField(max_length=15,null=True)
      
class Topic(models.Model):
    title = models.CharField(max_length = 10)
    questions = models.ForeignKey(to=Student,on_delete=models.CASCADE)
    date = models.DateTimeField()
    
      
class Revision_questions(models.Model):
      title = models.CharField(max_length = 10)
      date = models.DateTimeField()
      message = models.CharField(max_length = 20)
      answers = models.ForeignKey(to=Student,on_delete=models.CASCADE)
      
class Answers(models.Model):
      date = models.DateTimeField()
      message = models.CharField(max_length = 10)
      questions = models.ForeignKey(to=Student,on_delete=models.CASCADE)
