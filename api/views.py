from rest_framework import viewsets
from upeoapp import models
from .serializers import StudentSerializer,NotificationSerializer,TopicSerializer,AnswersSerializer,Revision_questionsSerializer

class StudentViewSets(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer

class NotificationViewSets(viewsets.ModelViewSet):
    queryset = models.Notification.objects.all()
    serializer_class = NotificationSerializer
    
class TopicViewSets(viewsets.ModelViewSet):
    queryset = models.Topic.objects.all()
    serializer_class = TopicSerializer
    
class Revision_questionsViewSets(viewsets.ModelViewSet):
    queryset = models.Revision_questions.objects.all()
    serializer_class = Revision_questionsSerializer
    
class AnswersViewSets(viewsets.ModelViewSet):
    queryset = models.Answers.objects.all()
    serializer_class = AnswersSerializer
    
