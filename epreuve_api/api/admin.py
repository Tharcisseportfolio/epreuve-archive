from django.contrib import admin
from api.models import Course, Epreuve, Exetat, File, Grade, Section,SendEmail,ContactMessage

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade', 'section')
    list_filter = ('grade', 'section')
    search_fields = ('name', 'grade', 'section')
class SendEmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'email', 'message', 'sent_at')
    list_filter = ('sent_at',)
    search_fields = ('subject', 'email', 'message', 'sent_at')

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'email', 'message', 'received_at')
    list_filter = ('received_at',)
    search_fields = ('subject', 'email', 'message', 'received_at')

class SectionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class GradeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class EpreuveAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'link','type','date')
    list_filter = ('course', 'date')
    search_fields = ('name', 'course', 'type','date')

class ExetatAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'link','type', 'date')
    list_filter = ('course', 'date')
    search_fields = ('name', 'course',type, 'date')

class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'link')
    list_filter = ('type', 'link')
    search_fields = ('name','type', 'link')

admin.site.register(SendEmail, SendEmailAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Epreuve, EpreuveAdmin)
admin.site.register(Exetat, ExetatAdmin)
admin.site.register(File, FileAdmin)