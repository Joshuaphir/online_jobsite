from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from users.models import User
from job.models import Job, AppliedJob

# Create your views here.
def dashboard(request):
    if request.user.is_applicant:
        jobs = Job.objects.order_by('-timestamp')[:5]
        userOnly = request.user
        profile = model_to_dict(userOnly)
        appliedjobs = AppliedJob.objects.filter(user=request.user)[:5]
        context = {
            'jobs':jobs,
            'profile':profile,
            'appliedjobs':appliedjobs
        }
        return render(request, 'dashboard/applicant/applicant-dashboard.html',context)
    elif request.user.is_recruiter:
        return render(request, 'dashboard/recruiter/recruiter-dashboard.html')

def home(request):
    return render(request, 'dashboard/home.html')

def recruiter_setting(request):
    Setting = "Setting"
    context = {
        'title': Setting
    }
    return render(request, 'company/settings.html', context)

def recruiter_jobs(request):
    return render(request, 'company/jobs.html')


def account_setting(request):
    Setting = "Account setting"
    context = {
        'title': Setting
    }
    return render(request, 'dashboard/recruiter/account-setting.html', context)