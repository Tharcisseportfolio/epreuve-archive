from django.contrib import admin
from api.models import *


@admin.register(SendEmail)
class SendEmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'email', 'message', 'sent_at')
    list_filter = ('sent_at',)
    search_fields = ('subject', 'email', 'message', 'sent_at')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'email', 'message', 'received_at')
    list_filter = ('received_at',)
    search_fields = ('subject', 'email', 'message', 'received_at')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','course', 'grade', 'section']
    list_filter = ['grade', 'course','section']
    search_fields = ['course', 'grade', 'section']

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['id','section']
    list_filter = ['section']
    search_fields = ['section']

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['id','course','section','test','link','year']
    list_filter = ['course','section','test','link','year']
    search_fields = ['course','section','test','link','year']

