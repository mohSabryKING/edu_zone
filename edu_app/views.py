from django.http import HttpResponse
from django.shortcuts import *
from django.views.generic.base import *
from django.views.generic.edit import FormView
from django.views.generic.list import *
from django.views.generic import View,CreateView
from django.contrib import messages as msg
import random as ran
from .models import *
from .form_x import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import *
from django.http import HttpResponseRedirect
from django.urls import *
from django.contrib.auth.views import *




class Login_model(LoginView):
    def get_success_url(self):
        return reverse_lazy('home',kwargs={'pk': self.request.user.pk, 'name': self.request.user.username})


class Logout_phase(LogoutView):
    template_name="logout.html"




# Create your views here.


'''
          context['subj']=[Course.objects.create(pk=i) for i in range(20)]
          context['master']=[Teacher.objects.create(pk=i) for i in range(10)]
          context['subj_ch']=[Course_chapter.objects.create(pk=i) for i in range(30)]
          context['Exams']=[Exams.objects.create(pk=i) for i in range(15)]




          context['subj']=Course.objects.count()
          context['subj_cont']=Course.objects.all()
          context['master']=Teacher.objects.count()
          context['subj_ch']=Course_chapter.objects.count()
          context['exams']=Exams.objects.count()






'''
'''class Login_model(auth_x.LoginView):
    def action(self):
        print("\n\n\nLOGGED IN \n\n")


class Logout_model(auth_x.LogoutView):
    def action(self):
        print("\n\n\nLOGGED OUT \n\n")
'''


class Register_form(View):

    def post(self,h):
            add_user=Add_user(h.POST)
            if add_user.is_valid():
                print("user data saved")
                add_user.save()
                print("\n\n\n"+str(add_user)+"\n\n\n")
                msg.success(h,"data saved")
                return redirect('your_op')
            else:
                msg.error(h,"data wasnt saved or repeated")
            
            return render(h,'add_user.html',{'form':add_user})
    
    def get(self,h):
            add_user=Add_user()
            return render(h,'add_user.html',{'form':add_user})
    

def register_fun(h):
    if h.method=="POST":
        print("POST ACTION CALLED")
        add_user=Add_user(h.POST)
        if add_user.is_valid():
            print("IT IS VAILD")
            trac=add_user.save()
            login(h,trac)
            print(trac)
            return redirect('your_op')
        else:
            print("NOT VAILD")
    else:
        add_user=Add_user()
        print("NO POST ACTION CALLED")
    return render(h,'add_user.html',{'form':add_user})

    
    
    
    


def redirect_action(h):
    return redirect('home')








class Menu_view(TemplateView):
      template_name="home.html"
      def get_context_data(self, **kwargs):
          context = super(Menu_view, self).get_context_data(**kwargs)
          #context['subj']=[Course.objects.create(pk=i) for i in range(20)]
          #context['master']=[Teacher.objects.create(pk=i) for i in range(10)]
          #context['subj_ch']=[Course_chapter.objects.create(pk=i) for i in range(30)]
          #context['exams']=[Exams.objects.create(pk=i) for i in range(15)]
          context['subj']=Course.objects.count()
          context['subj_cont']=Course.objects.all()[:10]
          context['master']=Teacher.objects.count()
          context['master_c']=Teacher.objects.all()[:5]
          context['subj_ch']=Course_chapter.objects.count()
          context['exams']=Exams.objects.count()
          print("OBJECS CER")
          return context
      


def get_user_key(u):
    return User.objects.get(pk=u)

def master_or_stu(h):
    user_x=h.user.username
    return render(h,'master__stu.html',{'u':user_x})



     







def menu(h):
    context={
          ''''subj':[Course.objects.create(id=i) for i in range(20)]
          ,'master':[Teacher.objects.create(pk=i) for i in range(10)]
          ,'subj_ch':[Course_chapter.objects.create(pk=i) for i in range(30)]
          ,'exams':[Exams.objects.create(pk=i) for i in range(15)]'''
          
          
          'subj':Course.objects.count()
          ,'subj_cont':Course.objects.all()
          ,'master':Teacher.objects.count()
          ,'subj_ch':Course_chapter.objects.count()
          ,'exams':Exams.objects.count()


    }
    return render(h,'home.html',context)



class Make_stu_profile(CreateView):
    template_name="stu_profile_make.html"
    form_class=Build_stu_profile
    model=Stu_profile
    #pk_url_kwarg='u'
    success_url=reverse_lazy("home")
    
    
    
    
    


class MasterList(ListView):
    model = Teacher
    context_object_name = 'masters_list'
    template_name='masters.html'
'''
لازم نكون مسجل هنا في الموقع
'''

##@login_required

class Make_master_profile(CreateView):
    template_name="master_profile_make.html"
    form_class=Build_master_profile
    model=Teacher
    pk_url_kwarg='m_e'
    success_url=reverse_lazy("view_master_profile",pk_url_kwarg)
    
 
    
'''
لازم نكون مسجل هنا في الموقع
'''    
##@login_required

class Display_stu_profile(TemplateView):
    template_name="stu_profile_show.html"
    def get_context_data(self, **kwargs,):
        u_=kwargs.pop('u',None)
        context = super(Display_stu_profile, self).get_context_data(**kwargs)
        context['user']=User.objects.get(pk=u_)
        context['stu']=Stu_profile.objects.get(related_to=u_)
        return context

'''
لازم نكون مسجل هنا في الموقع

no pk for master profile
'''
#@login_required

def return_master_key(m_e):
    print("the master key is "+str(m_e))
    return  Teacher.objects.get(pk=m_e)









    
    

class Display_master_profile(TemplateView):
    template_name="master_profile_show.html"
    def get_context_data(self, **kwargs):
        c = kwargs.pop('m_e', None)
        context = super(Display_master_profile, self).get_context_data(**kwargs)
        context['user']=User.objects.get(pk=c)
        context['master']=Teacher.objects.get(related_to=c)
        context['master_exams']=Exams.objects.filter(created_by=c)
        return context


'''
بناء الشهادات للطلاب
'''

class Certifiacte_make(CreateView):
    model=Certifiacte
    form_class=Add_Certifiacte_file
    template_name='congrate_form.html'
    def get_context_data(self, **kwargs):
        context = super(Certifiacte_make, self).get_context_data(**kwargs)
        return context
   

class Certifiacte_lists(ListView):
    model = Certifiacte
    context_object_name = 'cong'
    template_name='congrate_lists.html'
    def get_context_data(self, **kwargs):
        context = super(Certifiacte_lists, self).get_context_data(**kwargs)
        return context

def display_certificate_model(h):

    return render(h,'congrate_model.html')



'''
بناء الملاخصات للطلاب
'''


class Make_Summery(CreateView):
    template_name='summery_add_form.html'
    success_url=reverse_lazy("stu_created")
    form_class=Add_Summery_file
    model=Summery
    

class Summery_List(ListView):
    model = Summery
    context_object_name = 'summery'
    template_name='summery_list.html'















'''
لازم نكون مسجل هنا في الموقع
'''
##@login_required

class Course_list(ListView):
    model = Course
    context_object_name = 'c_list'
    template_name='courses.html'

    def get_context_data(self, **kwargs):
        context = super(Course_list, self).get_context_data(**kwargs)
        return context


def video_detail(h,c,lesson):
    print("THE STUDENT VIDEO DONE")
    context={
        'course':Course.objects.get(pk=c),
        'ch':Course_chapter.objects.get(pk=lesson),
    }
    return render(h,'lesson.html',context)
'''
لازم نكون مسجل هنا في الموقع
'''
#@login_required

class Course_chapters_view(TemplateView):
    template_name='chapters.html'
    def get_context_data(self, **kwargs):
        
        c = kwargs.pop('c', None)
        context = super(Course_chapters_view, self).get_context_data(**kwargs)
        context['course']=Course.objects.get(pk=c)
        #context['ch_list']=[Course_chapter.objects.create(pk=i) for i in range(10)]
        context['ch_list']=Course_chapter.objects.filter(for_course=c)
        return context
    



class Add_Exam(CreateView):
    model=Exams
    form_class=Add_Exam_file
    success_url=reverse_lazy("stu_created")
    pk_url_kwarg='m_'
    template_name="exam_add_form.html"
    
    def form_valid(self, form):
        if form:
            return redirect('home')
        return super().form_valid(form)
    
def add_exam(h):
    if h.method=='POST':
        print("Post Action enabeld")

    else:
        print("NO Post Action")
    return render(h,'exam_add_form.html')
    



class Exams_List(ListView):
    model = Exams
    context_object_name = 'ex_list'
    template_name='exams.html'
    def get_context_data(self, **kwargs):
        context = super(Exams_List, self).get_context_data(**kwargs)
        c = kwargs.pop('c', None)
        lesson = kwargs.pop('lesson', None)
        ex = kwargs.pop('ex', None)
        context['course']=Course.objects.get(pk=c),
        context['ch']=Course_chapter.objects.get(for_course=lesson),
        context['ex']=Exams.objects.filter(for_course=c),
        return context
    



def e500(h):return render(h,"err\e500.html",context={'e':"SERVER ISSUE"})
def e400(h,e):return render(h,"err\e400.html",context={'e':e})
def e404(h,e):return render(h,"err\e404.html",context={'e':e})
def e403(h,e):return render(h,"err\e403.html",context={'e':e})