from django.shortcuts import render
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from .forms import CustomSignUpForm
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from .models import Module, Progress
from django.db.models import Count
from django.contrib.auth.models import User



# Create your views here.
#This veiw can only be access by auth users else redirect to login
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request,"users/index.html")

def welcome(request):
    return render(request,"users/welcome.html")
def login_view(request):
    form = AuthenticationForm(data=request.POST)

    if request.method == 'POST':
        
        username =request.POST['username']
        password =request.POST['password']
        user=authenticate(request,username=username,password=password)
        #if user login details are correct, they will be redirected to the appropriate page
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:#return them back with what was typed in
            return render(request,"users/login.html",{
                "messages":"login with the correct details",
                'form':form
            })
            #the next line will display the login page to the user
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request,"users/welcome.html",{
        "messages":"Logged out, please login"
    })
def signup_view(request):
    form = CustomSignUpForm(request.POST)

    if request.method == 'POST':
        username =request.POST['username']
        email = request.POST['email']
        password1 =request.POST['password1']


        user = User.objects.create_superuser(username, email=email, password=password1)
        user.save()
       #take the user to login page
        user=authenticate(request,username=username,password=password1)
        login(request, user)
        return render(request,"users/index.html")

    else:
         
        return render(request, 'users/signup.html', {'form': form})


# At this point, user is a User object that has already been saved
# to the database. You can continue to change its attributes
# if you want to change other fields.
 #user.save()
         #   login(request, user)  # Log in the user after sign-up
        
       # user=authenticate(request,username=username,password=password)

        


def complete_module(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    progress, created = Progress.objects.get_or_create(user=request.user, module=module)
    progress.completed = True
    progress.save()

    # You can return a JSON response for asynchronous updates
    return JsonResponse({'status': 'success', 'message': 'Module marked as completed'})

def view_module(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    Progress.objects.update_or_create(
        user=request.user,
        module=module,
        defaults={'last_accessed': timezone.now()}
    )
    return render(request, 'module_detail.html', {'module': module})

#A dashboard provides an overview of the student’s progress in all modules.
def student_dashboard(request):
    user_progress = Progress.objects.filter(user=request.user)
    completed_modules = user_progress.filter(completed=True).count()
    total_modules = Module.objects.count()
    
    progress_percentage = (completed_modules / total_modules) * 100 if total_modules > 0 else 0

    return render(request, 'users/index.html', {
        'user_progress': user_progress,
        'completed_modules': completed_modules,
        'total_modules': total_modules,
        'progress_percentage': progress_percentage
    })
