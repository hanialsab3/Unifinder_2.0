from django.conf.urls import url,include
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from .views import login_user, SignUp, UserEditView, ShowProfilePageView, EditProfilePageView, ShowUniversityProfilePageView, EditUniversityProfilePageView, CreateUniversityProfilePageView, CreateStudentProfilePageView
from . import views




urlpatterns = [
    # url(r'login/$',
    #     auth_views.LoginView.as_view(template_name='accounts/login.html'),
    #     name='login'),
    # url(r'logout/$',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/',views.register_user,name='signup'),
    path('login_user/',views.login_user, name='login'),
    path('edit_profile/',UserEditView.as_view(),name='edit_profile'),
    path('<int:pk>/profile', ShowProfilePageView.as_view(),name='show_profile_page'),
    path('<int:pk>/edit_profile_page', EditProfilePageView.as_view(),name='edit_profile_page'),
    path('<int:pk>/profile_university', ShowUniversityProfilePageView.as_view(),name='show_university_profile_page'),
    path('<int:pk>/edit_profile_page_university', EditUniversityProfilePageView.as_view(),name='edit_university_profile_page'),
    path('create_university_profile_page/', CreateUniversityProfilePageView.as_view(),name='create_university_profile_page'),
    path('create_student_profile_page/', CreateStudentProfilePageView.as_view(),name='create_student_profile_page'),


]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
