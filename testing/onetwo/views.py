from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import HttpResponse
from .models import Video
# Create your views here.
def home(request):
    return render(request,'onetwo/home.html')
@login_required(login_url='sin')
def videos(request):
    vid = Video.objects.all()
    return render(request,'onetwo/videos.html', {'vid': vid})

@login_required(login_url='sin')
def lesson(request):
    return render(request, 'onetwo/lessons.html')
def subvideo(request):
    return render(request, 'onetwo/sub-videos.html')
def note(request):
    return render(request, 'onetwo/notes.html')
def tryy(request):
    return render(request, 'onetwo/try.html')
def live(request):
    return render(request, 'onetwo/stream.html')






def reg(request):
    if request.user.is_authenticated:
        return redirect('lessons')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']

            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname

            myuser.save()

            messages.success(request, 'your Account has been successfully created')
            return redirect('sin')
        return render(request, 'onetwo/sign-up.html')
def sign_out(request):
    logout(request)
    messages.success(request, 'logged Out Successfully')
    return redirect('home')

def sin(request):
    if request.user.is_authenticated:
        return redirect('lessons')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            pass1 = request.POST['pass1']

            user = authenticate(username=username, password=pass1)

            if user is not None:
                login(request, user)
                messages.info(request, 'you have successfully logged in ')
                return render(request, 'onetwo/lessons.html')

            else:
                messages.error(request, "User name or password is incorrect")

        return render(request, 'onetwo/signin.html')
