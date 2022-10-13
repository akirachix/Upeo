from django.urls import path, include
from rest_framework import routers


from .views import StudentViewSets,NotificationViewSets,TopicViewSets,AnswersViewSets,Revision_questionsViewSets

router = routers.DefaultRouter()
router.register(r"Student",StudentViewSets)
router.register(r"Notification",NotificationViewSets)
router.register(r"Topic",TopicViewSets)
router.register(r"Revision_questions",Revision_questionsViewSets)
router.register(r"Answers",AnswersViewSets)


urlpatterns = [
    path("",include(router.urls))
    
]
