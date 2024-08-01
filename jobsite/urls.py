from django.urls import path
from . import views
urlpatterns = [
    path('applicant-joblist/', views.joblist_view, name='applicant-joblist'),
    path('', views.jobsite, name='home-jodsite'),
    path('jobdetails/<int:pk>', views.job_detail, name='jobdetails')
]