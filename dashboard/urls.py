from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),
    path('recruiter-settings/', views.recruiter_setting, name='recruiter_setting'),
    path('recruiter-jobs/', views.recruiter_jobs, name='recruiter_jobs'),
    #path('account-settings/', views.account_setting, name='account_setting')
]