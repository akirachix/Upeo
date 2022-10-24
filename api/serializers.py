from upeoapp import  models
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ("phone_number",)
        fields = ("phone_number",)
        
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notification
        fields = ("message","origin","destination","status","title")

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Topic
        fields = ('topic','date','student')
        
class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answers
        fields = ('date', 'student','questions','topic',)

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Questions
        fields = ('question', 'student','date','answers','topic',)
        
class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Form
        fields = ('form','questions','student','answers','topic')
        
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
         model = models.Login
         fields = ("email","password")
         
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
         model = models.Signup
         fields = ('first_name','last_name','email', 'password','confirm_password')
    
    

    
        
