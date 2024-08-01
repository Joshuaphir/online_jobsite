from django.shortcuts import render, redirect
from job.models import Job, AppliedJob

# Create your views here.
def jobsite(request):
    return render(request, 'jobsite/home.html')

#joblist for applicant
def joblist_view(request):
    jobs = Job.objects.filter(is_available = True).order_by('-timestamp')
    context = {'jobs':jobs}
    return render(request, 'dashboard/applicant/job-listing.html', context)

#job details for applicant
def job_detail(request, pk):
    if AppliedJob.objects.filter(user=request.user, job=pk).exists():
        has_applied = True
    else:
        has_applied = False
    job = Job.objects.get(pk=pk)
    context = {'job':job}
    return render(request, 'dashboard/applicant/job-details.html', context)
