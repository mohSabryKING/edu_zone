from typing import Self
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from .views import *

user_y=''
def show_user(val): return val






print("jjjjjjjjj")
print(user_y)
print("jjjjjjjjj")

class Add_user(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2')


#class Build_stu_profile():pass


class Build_master_profile(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets={
            'name':forms.TextInput()
        }


#username_x=show_user
#print(username_x)
class Build_stu_profile(forms.ModelForm):
    class Meta:
        model = Stu_profile
        fields = ('related_to','stu_img_1','stu_img_2','name','phone','age')
        widgets={
           #'related_to':forms.TextInput(attrs={'class':'jjjj'})
        }
       


class Add_Exam_file(forms.ModelForm):
    class Meta:
        model=Exams
        fields="__all__"
        widgets={
           'bio':forms.Textarea(attrs={}),
        }





class Add_Summery_file(forms.ModelForm):
    class Meta:
        model=Summery
        fields="__all__"
        widgets={
        }



class Add_Certifiacte_file(forms.ModelForm):
    class Meta:
        model=Certifiacte
        fields="__all__"
        widgets={
        }