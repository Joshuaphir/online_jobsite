from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('applications/', views.applications_view, name='applications'),
    path('update-resume/', views.update_cV_view, name='update-cv-view'),
    path('dashboard/', views.dashboard_view, name='dashboard-view'),
]
