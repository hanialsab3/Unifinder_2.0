from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import ModelForm
from .models import University, Student, Application, Program

class ProfilePageStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('profile_picture','age','location','education','about')

        widgets = {
            'about': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.TextInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
            'education': forms.TextInput(attrs={'class':'form-control'}),
            'about': forms.TextInput(attrs={'class':'form-control'}),
        }

class ProfilePageUniverityForm(ModelForm):
    class Meta:
        model = University
        fields = ('profile_picture','website','name','phone','location','total_students','about')

        widgets = {
            # 'profile_picture': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'website': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),

            'about': forms.Textarea(attrs={'class':'form-control'}),
            'total_students': forms.NumberInput(attrs={'class':'form-control'}),
        }


class SignUpForm(UserCreationForm):                           #add init function in case the boostrap is messed up
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    def __init__(self,*args,**kwargs):
        super(SignUpForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = "form-control"
        self.fields['password1'].widget.attrs['class'] = "form-control"
        self.fields['password2'].widget.attrs['class'] = "form-control"
        self.fields['username'].widget.attrs['placeholder'] = "Enter your username"
        self.fields['password1'].widget.attrs['placeholder'] = "Enter your password"
        self.fields['password2'].widget.attrs['placeholder'] = "Enter your password again"
        self.fields['first_name'].widget.attrs['placeholder'] = "Enter your first name"
        self.fields['last_name'].widget.attrs['placeholder'] = "Enter your last name"
        self.fields['email'].widget.attrs['placeholder'] = "Enter your email"


class EditProfileForm(UserChangeForm):                           #add init function in case the boostrap is messed up
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    # username = forms.CharField(max_length=100)
    last_login = forms.CharField(max_length=100)
    is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput())
    is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput())
    is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput())
    date_joined = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined')


class UniversityForm(ModelForm):
    class Meta:
        model = University
        fields = ('user','profile_picture','name','website','phone','location','about')

        widgets = {
            'user': forms.TextInput(attrs={'class':'form-control','value':'','id':'use', 'type':'hidden'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'website': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
            'about': forms.Textarea(attrs={'class':'form-control'}),
        }

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('user','about',)

        widgets = {
            'user': forms.TextInput(attrs={'class':'form-control','value':'','id':'use', 'type':'hidden'}),
            'about': forms.TextInput(attrs={'class':'form-control'}),
        }



class UniversityProfileForm(ModelForm):
    class Meta:
        model = University
        fields = ('profile_picture','website','name','phone','location','about')

        widgets = {
            'profile_picture': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'website': forms.TextInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
            'about': forms.TextInput(attrs={'class':'form-control'}),
        }



        def __init__(self, *args, **kwargs):
            # self.fields['user'] = kwargs.pop('user', None)
            # print(user)
            print(user)
            if model.objects.filter(user=1).exists():
                raise ValidationError("This user name already created a University!!!")
            self.user = user
            super(UniversityProfileForm, self).__init__(*args, **kwargs)


class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = ('uni','name','description','profile_picture','tuition','requirements','location','deadline','duration','degree_studies','degree_studies',)

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'tut=ition': forms.Textarea(attrs={'class':'form-control'}),
        }
