from django.urls import path
from . import views

urlpatterns = [
    path ("",views.Student,name="registration"),
    path('',views.Student.as_view(),name="sendemail")

]
