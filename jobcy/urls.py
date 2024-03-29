"""jobcy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import ShowUniversityProfilePageView, ProgramDetailView

# urls.py

urlpatterns = [
    path('admin/clearcache/', include('clearcache.urls')),
    path('admin/', admin.site.urls),
    # Index Page
    path('', views.Index.as_view(),name='index'),
    path('index-2/', views.Index2.as_view(),name='index-2'),
    path('index-3/', views.Index3.as_view(),name='index-3'),

    # Company
    path('company/',include('company.urls')),

    # Pages
    path('pages/',include('django.contrib.auth.urls')),
    path('pages/',include('pages.urls')),

    # Accounts
    path('accounts/',include('accounts.urls')),

    # Blog
    path('blog/',include('blog.urls')),

    # Contact
    path('',include('contact.urls')),

    # Manage-Jobs
    path('manage-jobs',views.ManageJobs.as_view(),name='manage-jobs'),
    path('manage-jobs-post',views.ManageJobs.as_view(),name='manage-jobs-post'),
    path('bookmark-jobs',views.BookmarkJobs.as_view(),name='bookmark-jobs'),
    # path('profile',views.Profile.as_view(),name='profile'),

    path('<int:pk>/profile_university', ShowUniversityProfilePageView.as_view(),name='show_university_profile_page'),
    path('<int:pk>/programs', ProgramDetailView.as_view(), name='program'),
    path('programs/add<int:pk>', views.AddProgramView.as_view(), name='add-program'),
    # path('programs/add/', views.AddProgramView.as_view(), name='add_program'),
    # path('programs/edit/<int:pk>/', views.UpdateProgramView.as_view(), name='update_program'),
    path('programs/<int:pk>', views.DeleteProgramView.as_view(), name='delete-program'), # should be programs/delete/<int:pk>/
    path('add/<int:pk>', views.AddApplicationView.as_view(), name='add_application'), #should be applications/add/...
    path('search_universities', views.search_universities, name='search-universities'),
    path('applications_list/<int:pk>', views.ApplicationListView.as_view(), name='application-list'),
    path('applicants_list', views.applicants_list, name='applicants-list'),
    path('application/<int:pk>', views.ApplicationDetailView.as_view(), name='application-detail'),
    path('applications/<int:pk>', views.DeleteApplicationView.as_view(), name='delete-application'), # should be applications/delete/<int:pk>/


]+ static(settings.STATIC_URL,)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
