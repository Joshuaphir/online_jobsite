
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from . models import User
from . forms import RegisterUserForm
from resume.models import Resume
from company.models import Company


# register applicant only 
def register_applicant(request):
    form1 = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        #messages.success(request,  form)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_applicant = True
            var.save()
            Resume.objects.create(user=var)
            user = form.cleaned_data.get('username')
            messages.success(request, 'account has been created for' + user)
            return redirect('login')
        else:
            messages.error(request, 'something went wrong')
    context = {'form': form1}
    return render(request, 'users/register_applicant.html', context)

# register recruiter only 
def register_recruiter(request):
    form1 = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        #messages.success(request,  form)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_recruiter = True
            var.save()
            Company.objects.create(user=var)
            user = form.cleaned_data.get('username')
            messages.success(request, 'account has been created for' + user)
            return redirect('login')
        else:
            messages.error(request, 'something went wrong')
    context = {'form': form1}
    return render(request, 'users/register_recruiter.html', context)

    

# login a user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password) 
        if user is not None and user.is_active: 
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong') 
            return redirect('login')
    else:
        return render(request, 'users/login.html')
    
# logout a user
def logout_user(request):
    logout(request)
    #messages.info(request, 'you have logout successfully')
    return redirect('login')