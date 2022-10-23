from django import views
from django.urls import path, include
from rest_framework import routers


from .views import SignupViewSets, LoginViewSets, NotificationViewSets, StudentViewSets,TopicViewSets,AnswersViewSets,QuestionsViewSets

router = routers.DefaultRouter()
router.register(r"Student",StudentViewSets)
router.register(r"Notification",NotificationViewSets)
router.register(r"Topic",TopicViewSets)
router.register(r"Questions",QuestionsViewSets)
router.register(r"Answers",AnswersViewSets)
router.register(r"Login",LoginViewSets)
router.register(r"Signup",SignupViewSets)
# router.register(r"Form",FormViewSets)


urlpatterns = [
    path("",include(router.urls))
    
]
