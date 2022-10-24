from django.db import models
# from django.forms import CharField
# Create your models here

class Student(models.Model):
      phone_number = models.CharField(max_length = 15, null=True) 
      
class Topic(models.Model):
    topic = models.CharField(max_length = 10,null=True)
    student= models.ForeignKey(Student,on_delete=models.CASCADE,related_name='Upeo_student1')
    date = models.DateTimeField()
    
    
class Questions(models.Model):
      student= models.ForeignKey(Student,on_delete=models.CASCADE,related_name='Upeo_student4')
      date = models.DateTimeField()
      question= models.TextField(max_length = 160,null=True)
      topic= models.ForeignKey(Topic,on_delete=models.CASCADE,related_name='Upeo_questions5')
      answers= models.CharField(max_length= 20,null=True)
      
      
class Answers(models.Model):
      topic= models.ForeignKey(Topic,on_delete=models.CASCADE,related_name='Upeo_Topic7')
      date = models.DateTimeField()
      questions= models.ForeignKey(Questions,on_delete=models.CASCADE,related_name='Upeo_questions8')
      corect_answer = models.TextField(max_length = 50,null=True)
      student= models.ForeignKey(Student,on_delete=models.CASCADE,related_name='Upeo_student9')        


class Notification(models.Model):
      status = models.CharField(max_length = 6,null=True)
      STATUS_CHOICE = (
        ('read','read'),
        ('unread','unread'),
    )

      message = models.CharField(max_length = 15,null=True)
      origin = models.CharField(max_length = 6,null=True)
      destination = models.ForeignKey(to=Student,on_delete=models.CASCADE)
      title = models.CharField(max_length=15,null=True)
      
class Form (models.Model):
      student= models.ForeignKey(Student,on_delete=models.CASCADE,related_name='Upeo_student')
      form = models.IntegerField()
      topic= models.ForeignKey(Topic,on_delete=models.CASCADE,related_name='Upeo_Topic')
      questions= models.ForeignKey(Questions,on_delete=models.CASCADE,related_name='Upeo_questions')
      answers= models.ForeignKey(Answers,on_delete=models.CASCADE,related_name='Upeo_answers')
      
    

class Login(models.Model):
      email = models.EmailField()
      password = models.CharField(max_length = 40)
      
class Signup(models.Model):
      first_name = models.CharField(max_length=30,null=True)
      last_name = models.CharField(max_length=60,null=True)
      email = models.EmailField()
      password = models.CharField(max_length = 30)
      confirm_password = models.CharField(max_length = 30)
      