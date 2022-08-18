from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Student, University, Program, Application
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.core.paginator import Paginator
from accounts import forms
from .forms import ProgramForm, ApplicationForm
from django.urls import reverse_lazy

def search_universities(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        level = request.POST.get('level')
        # universities = University.objects.filter(name__contains=searched)
        # programs = Program.objects.filter(name__contains=searched).filter(level__contains=level) |  Program.objects.filter(name__contains=searched)
        p = Paginator(University.objects.filter(name__contains=searched) , 8)
        page = request.GET.get('page')
        universities = p.get_page(page)
        nums = "a" * universities.paginator.num_pages
        return render(request, 'search.html',{'searched':searched, 'universities': universities, 'nums': nums})
    else:                                              #coming from View More on index page
        p = Paginator(University.objects.all(), 8)
        page = request.GET.get('page')
        universities = p.get_page(page)
        nums = "a" * universities.paginator.num_pages
        return render(request, 'search.html',{'universities': universities, 'nums': nums})


class Index(TemplateView):
    template_name = "index/index-1.html"


    # def get_queryset(self):
    #     return User.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        # if (current_user.is_staff):
        #     context['is_uni'] = True
        # else:
        #     context['is_uni'] = False
        context['students'] = Student.objects.all()[:5]
        context['universities'] = University.objects.all()[:5]

        return context

class Index2(TemplateView):
    template_name = "index/index-2.html"
class Index3(TemplateView):
    template_name = "index/index-3.html"

# Manage-Jobs Page
class ManageJobs(TemplateView):
    template_name = "manage-jobs.html"
class ManageJobsPost(TemplateView):
    template_name = "manage-jobs-post.html"
class BookmarkJobs(TemplateView):
    template_name = "bookmark-jobs.html"
# class Profile(TemplateView):
#     template_name = "profile.html"

class ShowUniversityProfilePageView(DetailView):
    model = University
    template_name = 'university-profile.html'

    def get_context_data(self, **kwargs):
        universities = University.objects.all()
        context = super(ShowUniversityProfilePageView, self).get_context_data(**kwargs)
        page_university = get_object_or_404(University, id=self.kwargs['pk'])
        context["page_university"] = page_university
        context['programs'] = Program.objects.filter( uni = page_university)
        return context

class ProgramDetailView(DetailView):
    model = Program
    template_name = 'program-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AddProgramView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'add_program.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_program_id = self.kwargs['pk']
        context['university_id'] = page_program_id
        return context

    def form_valid(self,form):
        form.instance.uni = get_object_or_404(University, id=self.kwargs['pk'])
        return super().form_valid(form)

# class UpdateProgramView(UpdateView):
#     model = Program
#     form_class = ProgramForm
#     template_name = 'update_program.html'
#     # fields =

class DeleteProgramView(DeleteView):
    model = Program
    template_name = 'delete-program.html'
    success_url = reverse_lazy('index')

class AddApplicationView(CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'add_application.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_program = get_object_or_404(Program, id=self.kwargs['pk'])
        context['program'] = page_program
        return context

    def form_valid(self,form):
        page_program = get_object_or_404(Program, id=self.kwargs['pk'])
        form.instance.uni = page_program.uni
        form.instance.program = page_program
        if (self.request.user.student):
            form.instance.student = self.request.user.student
        return super().form_valid(form)

class ApplicationDetailView(UpdateView):
    model = Application
    template_name = 'application_detail.html'
    fields = ['reviewed','accepted']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_application = get_object_or_404(Application, id=self.kwargs['pk'])
        context['application'] = page_application
        return context

class DeleteApplicationView(DeleteView):
    model = Application
    template_name = 'delete-application.html'
    success_url = reverse_lazy('index')

class ApplicationListView(TemplateView):
    template_name = 'application-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_student = get_object_or_404(Student, id=self.kwargs['pk'])
        context['applications'] = Application.objects.filter( student = page_student)
        return context

def applicants_list(request):
    current_university = request.user.university
    applications = Application.objects.filter(uni = current_university)
    programs = Program.objects.filter(uni = current_university)

    if request.method == "POST":
        program = request.POST.get('program_filter')
        if (program == '-1'):
            p = Paginator(Application.objects.filter(uni=current_university), 10)
            page = request.GET.get('page')
            apps = p.get_page(page)
            nums = "a" * apps.paginator.num_pages
        else:
            p = Paginator(Application.objects.filter(uni=current_university, program=program),10)
            page = request.GET.get('page')
            apps = p.get_page(page)
            nums = "a" * apps.paginator.num_pages
        return render(request, 'applicants-list.html',{'apps':apps, 'programs':programs,'nums':nums})
    else:
        p = Paginator(Application.objects.filter(uni=current_university), 10)
        page = request.GET.get('page')
        apps = p.get_page(page)
        nums = "a" * apps.paginator.num_pages
        return render(request, 'applicants-list.html',{'apps':apps, 'applications':applications, 'programs':programs, 'nums':nums})

# class ApplicantsListView(TemplateView):
#     template_name = 'applicants-list.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         current_university = self.request.user.university
#         applications = Application.objects.filter(uni = current_university)
#         programs = Program.objects.filter(uni = current_university)
#         context['applications'] = applications
#         context['programs'] = programs
#         return context
#
#     def form_valid(self,form):
#         print(self.request.POST.get('program_filter'))
#
#         return super().form_valid(form)
