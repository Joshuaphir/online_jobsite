from django.urls import path
from . import views
urlpatterns = [
    path('update-company/', views.update_company, name='update-company'),
    path('company-profile/', views.company_profile, name='company-profile'),
    path('company-detail/<int:pk>', views.company_details, name='company-detail')  
]