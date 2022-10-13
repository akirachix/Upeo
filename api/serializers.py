from dataclasses import field
from upeoapp import  models
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ("first_name","last_name","admission_number","pin")
        
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
        
class Revision_questionsSerializer(serializers.ModelSerializer):
    class Meta:
     model = models.Revision_questions
    fields = ("date","answers","message","title")
