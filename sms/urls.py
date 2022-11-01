from django.urls import path

from . import views

urlpatterns = [
    # path("send_sms",views.send_sms,name="send_sms"),
        path("send_sms",views.send,name="send_sms"),


    
]




