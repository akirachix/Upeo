from django.contrib import admin

from .models import  Notification,Student,Login,Signup,Form,Topic,Questions,Answers


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('phone_number',)
    search_fields = ('phone_number',)
admin. site.register(Student,StudentAdmin)



class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'status', 'STATUS_CHOICE','title')
    search_fields = ('message', 'status','STATUS_CHOICE','title')
admin. site.register(Notification,NotificationAdmin)


class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic','date','student')
    search_fields = ('topic','date','student')
admin. site.register(Topic,TopicAdmin)


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('question', 'student','date','answers','topic',)
    search_fields = ('question', 'student''date','answers','topic',)
admin. site.register(Questions,QuestionsAdmin)


class AnswersAdmin(admin.ModelAdmin):
    list_display = ('date', 'student','questions','topic',)
    search_fields = ('date', 'student','questions','topic',)
admin. site.register(Answers,AnswersAdmin)

class LoginAdmin(admin.ModelAdmin):
    list_display = ('email', 'password',)
    search_fields = ('email', 'password',)
admin. site.register(Login,LoginAdmin)

class SignupAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email', 'password','confirm_password' )
    search_fields = ('first_name','last_name','email', 'password','confirm_password')
admin. site.register(Signup,SignupAdmin)


class FormAdmin(admin.ModelAdmin):
    list_display = ('form','questions','student','answers','topic')
    search_fields = ('form','questions','student','answers','topic')
admin. site.register(Form,FormAdmin)

