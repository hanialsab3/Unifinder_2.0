# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, SAFE_METHODS
from .serializers import UniversitySerializer, StudentSerializer, UserSerializer, ApplicationSerializer
from .models import University, Student, Application, Program
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm, ProfilePageUniverityForm, ProfilePageStudentForm, ProgramForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from . import forms
# Create your views here.

# def login_user(request):
#     return render(request, 'pages/extra-pages/sign-in.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')

        else:
            messages.success(request,("There was an error logging in, try again"))
            return redirect('login')

    else:
        return render(request, 'registration/login.html')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {
        'form':form,
    })

class CreateStudentProfilePageView(CreateView):
    model = Student
    form_class = ProfilePageStudentForm
    template_name = "registration/create_student_profile_page.html"

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CreateUniversityProfilePageView(CreateView):
    model = University
    form_class = ProfilePageUniverityForm
    template_name = "registration/create_university_profile_page.html"

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditProfilePageView(UpdateView):
    model = Student
    template_name = 'registration/edit_profile_page.html'
    fields = ['application_debug']
    success_url = reverse_lazy('home')


class ShowProfilePageView(DetailView):
    model = Student
    template_name = 'registration/student_profile.html'

    def get_context_data(self, **kwargs):
        students = Student.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        page_student = get_object_or_404(Student, id=self.kwargs['pk'])
        context["page_student"] = page_student
        return context


class EditUniversityProfilePageView(UpdateView):
    model = University
    template_name = 'registration/edit_university_profile_page.html'
    fields = ['profile_picture','website','name','phone','location','about']
    success_url = reverse_lazy('home')


# class ShowUniversityProfilePageView(DetailView):
#     model = University
#     template_name = 'pages/candidates-company/company-details.html'
#
#     def get_context_data(self, **kwargs):
#         universities = University.objects.all()
#         context = super(ShowUniversityProfilePageView, self).get_context_data(**kwargs)
#         page_student = get_object_or_404(University, id=self.kwargs['pk'])
#         context["page_student"] = page_student
#         context['programs'] = Program.objects.all()
#         return context

class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserEditView(UpdateView):
    form_class = EditProfileForm
    success_url = reverse_lazy('home')
    template_name = 'registration/edit_profile.html'

    def get_object(self):
        return self.request.user

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly)


class UniversityViewSet(viewsets.ModelViewSet):
    serializer_class = UniversitySerializer
    queryset = University.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly)    #IsAuthenticatedOrReadOnly



class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, DjangoModelPermissions)


class ApplicationUserWritePermission(BasePermission):
    message = "Editing application is restricted to the student only."


    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.student.user == request.user


class ApplicationViewSet(viewsets.ModelViewSet, ApplicationUserWritePermission):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()            #.filter(uni=..)
    authentication_classes = (TokenAuthentication,)
    permission_classes = [ApplicationUserWritePermission]

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [ApplicationUserWritePermission]
        else:
            permission_classes = [ApplicationUserWritePermission]
        return [permission() for permission in permission_classes]
