from django.shortcuts import render, redirect
from users.models import User
from django.contrib import messages
#from job.models import Job, AppliedJob
from django.forms.models import model_to_dict
from resume.models import Resume
from resume.forms import UpResumeForm

from django.shortcuts import render

def profile_view(request):
    userOnly = request.user
    profile = model_to_dict(userOnly)
    context = {
        'profile':profile,
    }
    return render(request, 'dashboard/applicant/profile.html', context)

def applications_view(request):
    return render(request, 'dashboard/applicant/applications.html')


def settings_view(request):
    return render(request, 'dashboard/applicant/settings.html')

def update_cV_view(request):
    if request.user.is_applicant:
        resume = Resume.objects.get(user=request.user)
        if request.method == "POST":
            form = UpResumeForm(request.POST, instance=resume)
            if form.is_valid():
                value = form.save(commit=False)
                user = User.objects.get(id=request.user.id)
                user.has_resume = True
                value.save()
                user.save()
                messages.info(request, 'CV information updated successfully')
                return redirect('dashboard')
            else:
                messages.error(request, 'something went wrong')
        else:
            form = UpResumeForm(instance=resume)
            context = {'form': form}
            return render(request, 'dashboard/applicant/update-resume.html', context)
    else:
        messages.warning(request, 'Permission Denied')
        return redirect('dashboard')

def dashboard_view(request):
    return render(request, 'dashboard/applicant/applicant-dashboard.html')
