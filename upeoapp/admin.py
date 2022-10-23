from django.contrib import admin

from .models import Answers, Notification,Questions, Student, Topic,Login,Signup


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'admission_number')
    search_fields = ('first_name', 'last_name','admission_number')
admin. site.register(Student,StudentAdmin)



class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'status', 'STATUS_CHOICE','title')
    search_fields = ('message', 'status','STATUS_CHOICE','title')
admin. site.register(Notification,NotificationAdmin)


class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'questions','date',)
    search_fields = ('title', 'questions''date',)
admin. site.register(Topic,TopicAdmin)


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'message','date','answers')
    search_fields = ('title', 'message''date','answers')
admin. site.register(Questions,QuestionsAdmin)


class AnswersAdmin(admin.ModelAdmin):
    list_display = ('date', 'message','questions')
    search_fields = ('date', 'message''questions')
admin. site.register(Answers,AnswersAdmin)

class LoginAdmin(admin.ModelAdmin):
    list_display = ('email', 'password',)
    search_fields = ('email', 'password',)
admin. site.register(Login,LoginAdmin)

class SignupAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email', 'password','confirm_password' )
    search_fields = ('first_name','last_name','email', 'password','confirm_password')
admin. site.register(Signup,SignupAdmin)


# class FormAdmin(admin.ModelAdmin):
#     list_display = ('form','questions','phone_number')
#     search_fields = ('form','questions','phone_number')
# admin. site.register(Form,FormAdmin)

