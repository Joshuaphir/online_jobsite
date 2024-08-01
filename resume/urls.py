from django.urls import path
from . import views

urlpatterns = [
    path('update-resume/', views.update_resume, name='updateResume'),
    path('resume-detail/<int:pk>', views.resume_details, name='resume-detail')  
]