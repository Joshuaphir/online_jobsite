from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from users.models import User
from django.views.generic import View
from . models import Job,AppliedJob
from . forms import CreateJobForm, UpdateJobForm

#create a job

def create_job(request):
    if request.user.is_recruiter and request.user.has_company:
        if request.method == "POST":
            form = CreateJobForm(request.POST)
            if form.is_valid():
                value = form.save(commit=False)
                value.user = request.user
                value.company = request.user.company
                value.save()
                messages.info(request, 'New Job created')
                return redirect('dashboard')
            else:
                messages.error(request, 'something went wrong')
        else:
            form = CreateJobForm()
            context = {'form': form}
            return render(request, 'dashboard/recruiter/job/create_job.html', context)
    else:
        messages.warning(request, 'Permission Denied')
        return redirect('dashboard')

#update job, recruiter section
def update_job(request, pk):
    job = Job.objects.get(pk=pk)
    if request.method == "POST":
        form = UpdateJobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.info(request, 'job updated successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'something went wrong')
            return redirect('recruiter-joblist')
    else:
        form = UpdateJobForm(instance=job)
        context = {'form': form}
        return render(request, 'dashboard/recruiter/job/update-job.html', context)
    
#see all jobs created by recruiter
def my_jobs(request):
    jobs = Job.objects.filter(user=request.user,company=request.user.company)
    context = {'jobs':jobs}
    return render(request, 'dashboard/recruiter/job-listing.html', context)

#applicant
def apply_to_job(request, pk):
    if request.user.is_authenticated:
        job = Job.objects.get(pk=pk)
        if AppliedJob.objects.filter(user=request.user, job=pk).exists():
            messages.info(request, 'You have already applied for this job')
            return redirect('dashboard')
        else:
            AppliedJob.objects.create(
                job= job,
                user = request.user,
                status = 'Pending'
            )
            messages.info(request, 'You have successfully applied for this Job')
            return redirect('dashboard')
    else:
        messages.info(request, 'You must login to apply')
        return redirect('login')

#get applicants for a job
def get_all_applicants_job(request, pk):
    job = Job.objects.get(pk=pk)
    applicants = job.AppliedJob_set_all()
    context = {'job':job, 'applicants':applicants}
    return render(request, 'dashboard/recruiter/applications.html', context)

#recruiter section
def get_all_applicants(request):
    applicants = AppliedJob.objects.all()
    context = {'applicants':applicants}
    return render(request, 'dashboard/recruiter/applications.html', context)

#recruiter job details
def job_detail_recruiter(request, pk):
    job = Job.objects.get(pk=pk)
    context = {'job':job}
    return render(request, 'dashboard/recruiter/job/job-details.html', context)

#recruiter delete job?
class JobDeleteView(View):
    def post(self, request, pk):
        job = get_object_or_404(Job, pk=pk)
        job.delete()
        return redirect('recruiter-joblist')