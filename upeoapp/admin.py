from django.contrib import admin

from .models import Answers, Notification, Revision_questions, Student, Topic

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'admission_number','pin', )
    search_fields = ('first_name', 'last_name','admission_number','pin',)
admin. site.register(Student,StudentAdmin)


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'status', 'STATUS_CHOICE','title', )
    search_fields = ('message', 'status','STATUS_CHOICE','title',)
admin. site.register(Notification,NotificationAdmin)


class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'questions','date', )
    search_fields = ('title', 'questions''date',)
admin. site.register(Topic,TopicAdmin)


class Revision_questionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'message','date','answers', )
    search_fields = ('title', 'message''date','answers', )
admin. site.register(Revision_questions,Revision_questionsAdmin)


class AnswersAdmin(admin.ModelAdmin):
    list_display = ('date', 'message','questions', )
    search_fields = ('date', 'message''questions',)
admin. site.register(Answers,AnswersAdmin)

