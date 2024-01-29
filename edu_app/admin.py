from django.contrib import admin
from .models import *
from django.contrib.auth.models import *







class Edu_admin(admin.AdminSite):
    site_title="المدرسه التعليميه"
    logout_template="logout.html"
    login_template="login.html"



admin.site=Edu_admin(name='edu_admin')


# Register your models here.
class Course_Admin(admin.ModelAdmin):pass
class Course_chapter_Admin(admin.ModelAdmin):pass
class Teacher_Admin(admin.ModelAdmin):
    list_display=[
        'pk','name','profile_link'
    ]

class Certifiacte_Admin(admin.ModelAdmin):pass

class Exams_Admin(admin.ModelAdmin):pass

class User_Admin(admin.ModelAdmin):
    list_display = ('pk','username',)




admin.site.site_header=" إداره الموقع التعليمي"
admin.site.site_title="الأداره"
admin.site.login_template='login.html'
admin.site.logout_template='logout.html'


admin.site.register(Course, Course_Admin)
admin.site.register(Course_chapter, Course_chapter_Admin)
admin.site.register(Teacher, Teacher_Admin)
admin.site.register(Certifiacte,Certifiacte_Admin)
admin.site.register(Exams,Exams_Admin)
admin.site.register(User,User_Admin)
admin.site.register(Group)

admin.site.register(Stu_profile)



