from django.contrib import admin
from .models import Student, Parent, Result, Department, Course, Grade, Semester, Session, Level
# Register your models here.
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['student','course', 'grade']
    search_fields = ['student__reg_no', 'course__code']
    list_filter= ['course__code', 'session__session']

admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(Semester)
admin.site.register(Session)
admin.site.register(Level)
