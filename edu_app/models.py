from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.html import format_html
from .exam_validation import *
# Create your models here.

cont_model='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Distinctio magni quaerat, eius, harum, voluptatem nostrum exercitationem aspernatur consectetur quibusdam non alias cum eveniet tempore delectus officiis sint fugiat laborum unde?'
class Stu_profile(models.Model):
    Div={('1-6','1-6'),('6-15','6-15'),('15-18','15-18'),('18-25','18-25')}
    related_to=models.OneToOneField(User,on_delete=models.CASCADE,null=True,related_name='stu_to')
    name= models.CharField(max_length=50,default="Mohamed zain")
    
    phone=models.PositiveBigIntegerField(default=201094128969,verbose_name="رقم الهاتف")
    stu_img_1 = models.ImageField(upload_to='stu_profile_img',default="user.png", max_length=100)
    stu_img_2 = models.ImageField(upload_to='stu_bkg_img', default="seo.jpg", max_length=100)
    #help
    age = models.IntegerField(default=6)
    added_in = models.DateField(auto_now=True)
    
    class Meta:verbose_name_plural="صفحه الطالب"
    def __str__(self):
        return self.name
    def type_model(self): return "student"
    def stu_type(self): return "student"
    

class Course(models.Model):
    Div={
        "C1":"Class 1",
        "C2":"Class 2",
        "C3":"Class 3",
        "C4":"Class 4",
        "C5":"Class 5",
        "C6":"Class 6",
        "C7":"Class 7",
        "C8":"Class 8",
        "C9":"Class 19",
        "C10":"Class 10",
        "C11":"Class 11",
        "C12":"Class 12",
    }
    c_name= models.CharField(max_length=50,default="Math 1")
    #help
    stu_div = models.CharField(max_length = 4, choices=Div ,default=Div["C1"])
    logo = models.ImageField(upload_to='stu_bkg_img', default="sm.jpg", max_length=100)
   
    bio = models.TextField(max_length=1500,default=cont_model)
    #added_in = models.DateField(auto_now=True)
    
    class Meta:verbose_name_plural="الماده العلميه"
    def __str__(self):
        return self.c_name
    


class Teacher(models.Model):
    related_to=models.OneToOneField(User,on_delete=models.CASCADE,null=True,related_name='master_to')
    name= models.CharField(max_length=50,default="وهدان محمود")
    phone=models.PositiveBigIntegerField(default=201094128969,verbose_name="رقم الهاتف")
    m_img_1 = models.ImageField(upload_to='master_profile_img',default="user.png", max_length=100)
    m_img_2 = models.ImageField(upload_to='master_bkg_img', default="seo.jpg", max_length=100)
    added_in = models.DateField(auto_now=True)
    class Meta:
        verbose_name_plural="المعلم"
        verbose_name="المعلم"
        
    def __str__(self):
        return str(self.pk)+":"+self.name
    def type_model(self): return "master"
    def profile_link(self):
        print("<a href='master_profile_"+str(self.related_to.pk-1)+" >{"+self.name+"} صفحه</a>")
        return format_html(f"<a href='master_profile_1' >{self.name} صفحه</a>")



class Course_chapter(models.Model):
    for_course = models.ForeignKey(Course, on_delete=models.CASCADE,null=True)
    #made_by= models.ForeignKey(Teacher, related_name='made_by', on_delete=models.CASCADE,blank=True,null=False,default="")
    title= models.CharField(max_length=100,default="Chapter model x")
    video = models.FileField(upload_to='coure_', max_length = 100,default="js_c.mp4")
    bio = models.TextField(max_length=1500,default=cont_model)
    added_in = models.DateField(auto_now=True)
    
    class Meta:verbose_name_plural="محنويات الماده"
    def __str__(self):
        return self.title






class Exams(models.Model):
    title= models.CharField(max_length=100,default="Exam y")
    #help
    exam_file = models.FileField(upload_to="exam made by/"+str(title), max_length = 50,default="exam_model.pdf")
    created_by= models.ForeignKey(Teacher, related_name='added_by_x', on_delete=models.CASCADE)
    #chapter_x= models.ForeignKey(Course_chapter, related_name='chapter_x', on_delete=models.CASCADE,blank=True,null=False)
    course_x= models.ForeignKey(Course, related_name='course_x', on_delete=models.CASCADE)
    bio = models.TextField(max_length=1500,default=cont_model)
    
    added_in = models.DateField(auto_now=True)
    class Meta:verbose_name_plural="أمتحانات"
    def exam_validation(self):pass
    def __str__(self):
        return str(self.pk)+":"+self.title


class Certifiacte(models.Model):
    title= models.CharField(max_length=50,default="Congrats")
    img_c = models.ImageField(upload_to='master_profile_img', height_field=None, width_field=None, max_length=100,default='seo.jpg')
    for_stu = models.ForeignKey(Stu_profile, on_delete=models.CASCADE,blank=True,null=False)
    in_chapter = models.ForeignKey(Course_chapter, on_delete=models.CASCADE,blank=True,null=False)
    deg = models.ForeignKey(Exams, on_delete=models.CASCADE,blank=True,null=False)
    
    added_in = models.DateField(auto_now=True)
    class Meta:verbose_name_plural="شهاده نقدير"
    def certifiacte_model(self):
        return format_html(f"<img height='120px' width='240px' src='{self.img_c.url}' />")
    def __str__(self):
        return str(self.pk)+":"+self.title




class Payments(models.Model):
    added_in = models.DateField(auto_now=True)
    class Meta:verbose_name_plural="الدفع"

class Summery(models.Model):
    title= models.CharField(max_length=70,default="Summery number")
    #help
    exam_file = models.FileField(upload_to="summery made by/"+str(title), max_length = 50,default="exam_model.pdf")
    created_by= models.ForeignKey(Teacher, related_name='added_by_x1', on_delete=models.CASCADE,verbose_name="")
    #chapter_x= models.ForeignKey(Course_chapter, related_name='chapter_x', on_delete=models.CASCADE,blank=True,null=False)
    course_x= models.ForeignKey(Course, related_name='course_x1', on_delete=models.CASCADE)
    bio = models.TextField(max_length=1500,default=cont_model)
    
    added_in = models.DateField(auto_now=True)