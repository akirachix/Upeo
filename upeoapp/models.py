from django.db import models
# from django.forms import CharField
# Create your models here

class Student(models.Model):
      first_name = models.CharField(max_length=15,null=True)
      last_name = models.CharField(max_length=15,null=True)
      admission_number = models.CharField(max_length=10,null=True)
      phone_number = models.CharField(max_length = 15, null=True)
      
      
class Topic(models.Model):
    title = models.CharField(max_length = 10)
    student= models.ForeignKey(Student,on_delete=models.CASCADE,related_name='Upeo_student1')
    questions= models.ForeignKey("Questions",on_delete=models.CASCADE,related_name='Upeo_questions2')
    answers= models.ForeignKey("Answers",on_delete=models.CASCADE,related_name='Upeo_answers3')
    date = models.DateTimeField()
    
    
class Questions(models.Model):
      student= models.ForeignKey(Student,on_delete=models.CASCADE,related_name='Upeo_student4')
      title = models.CharField(max_length = 10)
      date = models.DateTimeField()
      topic= models.ForeignKey(Topic,on_delete=models.CASCADE,related_name='Upeo_questions5')
      answers= models.ForeignKey("Answers",on_delete=models.CASCADE,related_name='Upeo_answers6')
      
class Answers(models.Model):
      topic= models.ForeignKey(Topic,on_delete=models.CASCADE,related_name='Upeo_Topic7')
      date = models.DateTimeField()
      questions= models.ForeignKey(Questions,on_delete=models.CASCADE,related_name='Upeo_questions8')
      title = models.CharField(max_length = 10)
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
      password = models.CharField(max_length = 10)
      
class Signup(models.Model):
      first_name = models.CharField(max_length=15,null=True)
      last_name = models.CharField(max_length=15,null=True)
      email = models.EmailField()
      password = models.CharField(max_length = 10)
      confirm_password = models.CharField(max_length = 10)
      