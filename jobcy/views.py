from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Student, University, Program, Application
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from accounts import forms
from accounts.forms import ApplicationForm

def search_universities(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        universities = University.objects.filter(name__contains=searched)
        return render(request, 'pages/candidates-company/candidate-list.html',{'searched':searched, 'universities': universities})
    else:
        return render(request, 'pages/candidates-company/candidate-list.html',{})


class Index(TemplateView):
    template_name = "index/index-1.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
class Profile(TemplateView):
    template_name = "profile.html"

class ShowUniversityProfilePageView(DetailView):
    model = University
    template_name = 'pages/candidates-company/company-details.html'

    def get_context_data(self, **kwargs):
        universities = University.objects.all()
        context = super(ShowUniversityProfilePageView, self).get_context_data(**kwargs)
        page_student = get_object_or_404(University, id=self.kwargs['pk'])
        context["page_student"] = page_student
        context['programs'] = Program.objects.all()
        return context

class ProgramDetailView(DetailView):
    model = Program
    template_name = 'pages/jobs/job-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# class AddProgramView(CreateView):
#     model = Program
#     form_class = ProgramForm
#     template_name = 'add_program.html'
#
# class UpdateProgramView(UpdateView):
#     model = Program
#     form_class = ProgramForm
#     template_name = 'update_program.html'
#     # fields =

class AddApplicationView(CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'pages/jobs/add_application.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_program = get_object_or_404(Program, id=self.kwargs['pk'])
        context['program'] = page_program
        return context

    def form_valid(self,form):
        page_program = get_object_or_404(Program, id=self.kwargs['pk'])
        form.instance.uni = page_program.uni
        if (self.request.user.student):
            form.instance.student = self.request.user.student
        return super().form_valid(form)

class ApplicationDetailView(DetailView):
    model = Application
    template_name = 'pages/jobs/application_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_program = get_object_or_404(Program, id=self.kwargs['pk'])
        context['program'] = page_program
        return context
