from django.db import models
# from django.forms import CharField
# Create your models here

class Student(models.Model):
      first_name = models.CharField(max_length=15,null=True)
      last_name = models.CharField(max_length=15,null=True)
      admission_number = models.CharField(max_length=10,null=True)
      # form = models.CharField(max_length=15)
      # phone_number = models.CharField(max_length=16,null=True)

class Form (models.Model):
      phone_number = models.ForeignKey(to=Student,on_delete=models.CASCADE)
      questions = models.ForeignKey(to=Student,on_delete=models.CASCADE)
      form = models.IntegerField()
      answers = models.ForeignKey(to=Student,on_delete=models.CASCADE)
          
      
class Notification(models.Model):
      status = models.CharField(max_length = 6,null=True)
      STATUS_CHOICE = (
        ('read','read'),
        ('unread','unread'),
    )

      message = models.CharField(max_length = 15,null=True)
      # phone_number = models.ForeignKey(to=Student,on_delete=models.CASCADE)
      origin = models.CharField(max_length = 6,null=True)
      destination = models.ForeignKey(to=Student,on_delete=models.CASCADE)
      title = models.CharField(max_length=15,null=True)
      
class Topic(models.Model):
    title = models.CharField(max_length = 10)
#     phone_number = models.ForeignKey(to=Student,on_delete=models.CASCADE)
    questions = models.ForeignKey(to=Student,on_delete=models.CASCADE)
    answers = models.ForeignKey(to=Student,on_delete=models.CASCADE)
    date = models.DateTimeField()
    
      
class Questions(models.Model):
      # phone_number = models.ForeignKey(to=Student,on_delete=models.CASCADE)
      title = models.CharField(max_length = 10)
      date = models.DateTimeField()
      message = models.CharField(max_length = 20)
      answers = models.ForeignKey(to=Student,on_delete=models.CASCADE)
      
class Answers(models.Model):
      date = models.DateTimeField()
      message = models.CharField(max_length = 10)
      questions = models.ForeignKey(to=Student,on_delete=models.CASCADE)
      # phone_number = models.ForeignKey(to=Student,on_delete=models.CASCADE)


class Login(models.Model):
      email = models.EmailField()
      password = models.CharField(max_length = 10)
      
class Signup(models.Model):
      first_name = models.CharField(max_length=15,null=True)
      last_name = models.CharField(max_length=15,null=True)
      email = models.EmailField()
      password = models.CharField(max_length = 10)
      confirm_password = models.CharField(max_length = 10)
      