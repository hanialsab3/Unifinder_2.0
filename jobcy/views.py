from django.views.generic import TemplateView
from accounts.models import Student, University

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
