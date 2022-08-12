# from django.contrib import auth
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.utils import timezone
from django.urls import reverse


# class User(auth.models.User, auth.models.PermissionsMixin):
#
#     def __str__(self):
#         return "@{}".format(self.username)
# class User(AbstractUser):
#     is_student = models.BooleanField('student status', default=False)
#     is_teacher = models.BooleanField('teacher status', default=False)

class University(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=120, null=True)
    website = models.CharField(max_length=120)
    email = models.CharField(max_length=120, null=True)
    phone = models.CharField(max_length=120, null=True)
    location = models.CharField(max_length=120, null=True)
    about = models.TextField(null=True)
    total_students = models.IntegerField(null=True, blank=True)

    def no_of_students(self):
        students = Student.objects.filter(uni=self)
        return len(students)

    def __str__(self):
        if self.name==None:
            return "ERROR-UNIVERSITY NAME IS NULL"
        return self.name

    def get_absolute_url(self):
        return reverse("show_university_profile_page", args=[str(self.id)])

class Student(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    about = models.TextField(null=True)
    # uni = models.ManyToManyField(University)
    profile_picture = models.ImageField(null=True, blank=True)
    age = models.CharField(max_length=120, null=True, blank=True)
    location = models.CharField(max_length=255, null=True)
    education = models.TextField(null=True)


    def __str__(self):
        if hasattr(self.user,'get_username'):
            return self.user.first_name + " " + self.user.last_name
        else:
            return "No Username"

    def get_absolute_url(self):
        return reverse("show_profile_page", args=[str(self.id)])

class Program(models.Model):
    name =  models.CharField(max_length=120)
    uni = models.ForeignKey(University, on_delete=models.CASCADE)
    description = models.TextField( null=True)
    profile_picture = models.ImageField(null=True, blank=True,default='featured-job/img-05.png')
    tuition = models.CharField(max_length=120, null=True)
    requirements = models.TextField(max_length=256, null=True)
    location = models.CharField(max_length=255, null=True)
    deadline = models.CharField(max_length=120, null=True)
    duration = models.CharField(max_length=120, null=True)
    degree_studies = models.CharField(max_length=120, null=True)
    level = models.CharField(max_length=120, null=True)


    def __str__(self):
        return  self.name

    def get_absolute_url(self):
        return reverse("program", args=[str(self.id)])

class Application(models.Model):
    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    uni = models.ForeignKey(University, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, null=True, on_delete=models.CASCADE)
    motivation = models.CharField(max_length=120)  #file
    cv = models.CharField(max_length=120)
    reviewed = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return "Application Number " + str(self.id)

    def get_absolute_url(self):
        return reverse("application-detail", args=[str(self.id)])
