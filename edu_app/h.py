from django.urls import path, re_path
from .views import *
from django.views.generic import *
from django.contrib.auth import views as auth_x
#from django.contrib.auth.urls import urlpatterns
#from edu_zone.settings import LOGIN_REDIRICT_URL
from django.contrib.auth.models import User
'''url_x="reg/"
auth_x.LoginView.success_url=url_x
print("displaying the values")
print(str(auth_x.LoginView.success_url))'''

urlpatterns = [
    path('login/',auth_x.LoginView.as_view(template_name='registration/login.html'),name="login")
      
    ,path('logout/',auth_x.LogoutView.as_view(template_name='registration/logout.html'),name="logout"),
   
    path('reg/',Register_form.as_view(),name="reg"),
    path('',Menu_view.as_view(),name='home'),
    #path('',menu,name='home'),
    
    path('master_or_stu',master_or_stu,name='your_op'),
    path('master_or_stu/stu',Make_stu_profile.as_view(),name='form_stu_profile'),
    path('master_or_stu/master',Make_master_profile.as_view(),name='form_master_profile'),






    path('master_profile_<int:m_e>/add_exam',Add_Exam.as_view(),name='add_exam'),
    path('stu_profile_<int:u>',Display_stu_profile.as_view(),name='view_stu_profile'),
    path('masters',MasterList.as_view(),name='masters'),
    path('master_profile_<int:m_e>',Display_master_profile.as_view(),name='view_master_profile'),
    #path('master_profile_<int:m_e>',return_master_key,name='call_master'),
    

    
    #path('accounts/profile/',redirect_action,name='redirect_now'),





#courses and thire links with exams   
    path('courses',Course_list.as_view(),name='sub_j'),
    path('courses/all_chapters_of_<str:c>',Course_chapters_view.as_view(),name='ch_subj'),
    path('courses/all_chapters_of_<int:c>/details_<int:lesson>',video_detail,name='subj_v'),
    path('courses/all_chapters_of_<int:c>/details_<int:lesson>/exam_<int:ex>',Exams_List.as_view(),name='exam'),
    #path('',Menu_view.as_view(),name='make_profile')
    
]