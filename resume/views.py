from django.shortcuts import render, redirect
from django.contrib import messages
from users.models import User
from . models import Resume
from . forms import UpResumeForm
# Create your views here.

def update_resume(request):
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
            return render(request, 'resume/update_resume.html', context)
    else:
        messages.warning(request, 'Permission Denied')
        return redirect('dashboard')

#viewing company
def resume_details(request, pk):
    resume = Resume.objects.get(pk=pk)
    context = {'resume': resume}
    return render(request, 'resume/resume_details.html', context)