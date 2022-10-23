# from dataclasses import field
from upeoapp import  models
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ("first_name","last_name","admission_number")
        
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notification
        fields = ("message","origin","destination","status","title")

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Topic
        fields = ("date","questions","title")
        
class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answers
        fields = ("date","questions","message")
        
class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Questions
        fields = ("date","answers","message","title")
        
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
         model = models.Login
         fields = ("email","password")
         
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
         model = models.Signup
         fields = ('first_name','last_name','email', 'password','confirm_password')
    
    

    
        
