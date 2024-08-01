from django.urls import path
from . import views

urlpatterns = [
    path('create-job/', views.create_job, name='create-job'),
    path('recruiter-joblist/', views.my_jobs, name='recruiter-joblist'),
    path('recruiter-jobdetails/<int:pk>/', views.job_detail_recruiter, name='recruiter-jobdetails'),
    path('recruiter-update-job/<int:pk>/', views.update_job, name='recruiter-update-job'),
    path('recruiter-job/<int:pk>/delete/', views.JobDeleteView.as_view(), name='recruiter-delete-job'),
    path('apply-job/<int:pk>/', views.apply_to_job, name='apply-job'),
    path('recruiter-applications/', views.get_all_applicants, name='recruiter-applications')  
]