from rest_framework import viewsets
from upeoapp import models
# from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import viewsets
from upeoapp import models
from .serializers import StudentSerializer,LoginSerializer,NotificationSerializer,TopicSerializer,AnswersSerializer,QuestionsSerializer,SignupSerializer,FormSerializer

class StudentViewSets(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer

class NotificationViewSets(viewsets.ModelViewSet):
    queryset = models.Notification.objects.all()
    serializer_class = NotificationSerializer
    
class TopicViewSets(viewsets.ModelViewSet):
    queryset = models.Topic.objects.all()
    serializer_class = TopicSerializer
        
class QuestionsViewSets(viewsets.ModelViewSet):
    queryset = models.Questions.objects.all()
    serializer_class = QuestionsSerializer
    
class AnswersViewSets(viewsets.ModelViewSet):
    queryset = models.Answers.objects.all()
    serializer_class = AnswersSerializer
    
class LoginViewSets(viewsets.ModelViewSet):
    queryset = models.Login.objects.all()
    serializer_class = LoginSerializer

class SignupViewSets(viewsets.ModelViewSet):
    queryset = models.Signup.objects.all()
    serializer_class = SignupSerializer
    
class FormViewSets(viewsets.ModelViewSet):
    queryset = models.Form.objects.all()
    serializer_class = FormSerializer

    
    
class StudentForm(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()
  
class Student(APIView):
    permission_classes = (permissions.AllowAny,)
    @swagger_auto_schema(request_body=StudentForm)
    def post(self, request):
        serializer = StudentForm(data=request.data)
        if serializer.is_valid():
            json = serializer.data
            return Response(
                data={"status": "OK", "message": json},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
