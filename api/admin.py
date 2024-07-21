from django.contrib import admin
from api.models import Course, Epreuve, Exetat, File, Grade, Section


admin.site.register(Grade)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Epreuve)
admin.site.register(Exetat)
admin.site.register(File)