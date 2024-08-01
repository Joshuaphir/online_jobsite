from django.shortcuts import render, redirect
from django.contrib import messages
from users.models import User
from . models import Company
from . forms import UpCompanyForm
# Create your views here.

def update_company(request):
    if request.user.is_recruiter:
        company = Company.objects.get(user=request.user)
        if request.method == "POST":
            form = UpCompanyForm(request.POST, instance=company)
            if form.is_valid():
                value = form.save(commit=False)
                user = User.objects.get(id=request.user.id)
                user.has_company = True
                value.save()
                user.save()
                messages.info(request, 'company information updated successfully')
                return redirect('dashboard')
            else:
                messages.error(request, 'something went wrong')
        else:
            form = UpCompanyForm(instance=company)
            context = {'form': form}
            return render(request, 'dashboard/recruiter/account-setting.html', context)
    else:
        messages.warning(request, 'Permission Denied')
        return redirect('dashboard')

#viewing company
def company_details(request, pk):
    company = Company.objects.get(pk=pk)
    context = {'company': company}
    return render(request, 'company/company_details.html', context)

def company_profile(request):
    return render(request, 'dashboard/recruiter/profile.html')