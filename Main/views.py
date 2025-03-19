from django.shortcuts import render,redirect
from Main.models import feedback_msg,WallpaperIMg
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def send_connec_us(email,first_name,last_name,country,msg):
    subject = f'{first_name} {last_name} from {country}'
    email_from = settings.EMAIL_HOST_USER
    message = msg
    send_mail(subject,message,email_from,[email])


def home(request):
    search_img = request.GET.get('search_img')

    if search_img != '' and search_img is not None:
        data = WallpaperIMg.objects.filter(wallpaperName__icontains=search_img)
        print(data)
        if data:
            return render(request,'wallpaper_view.html',{'data':data})
        
    return render(request,'index.html')


def user_login_register(request):
    if request.method == 'POST':
        if 'Submit_Register' in request.POST:
            #print("Registeration Form cha data yetoy")
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 != password2:
                messages.warning(request, "Password Does Not Match")
                return HttpResponseRedirect(request.path_info)

            #print(first_name,last_name,email,password1,password2)
            user = User.objects.filter(username = email)
            if user.exists():
                messages.warning(request, "Username already exits")
                return HttpResponseRedirect(request.path_info)

            user_obj = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=email)
        
            user_obj.set_password(password1)
            user_obj.save()
            return redirect('login')

        elif 'Submit_login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.filter(username = username)

            if not user.exists():
                messages.warning(request, "Account Not Found")
                return HttpResponseRedirect(request.path_info)
            
            user1 = authenticate(username=username,password=password)
            if user1:
                login(request,user1)
                return redirect('http://127.0.0.1:8000/')
            else:
                messages.warning(request, "Incorrect Password")
                return HttpResponseRedirect(request.path_info)
            
    return render(request,'loginpage.html')


def logout_user(request):
    logout(request)
    return redirect('login')


















def selected_wallpapers(request,choice):

    if choice != '' and choice is not None:
        data = WallpaperIMg.objects.filter(wallpaperName__icontains=choice)
        print(data)
        if data:
            return render(request,'wallpaper_view.html',{'data':data})
        
    redirect('home')


def connect_us(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        country = request.POST.get('country')
        message = request.POST.get('msg')
        email = 'bhoirraj872@gmail.com'
        
        feedback_msg.objects.create(
                                    first_name=first_name,
                                    last_name=last_name,
                                    country = country,
                                    msg = message
                                    )
        send_connec_us(email,first_name,last_name,country,message)
        
        #email = request.POST.get('email')
        #password = request.POST.get('password')
    return render(request,'connectus.html')

def about_us(request):
    return render(request,'aboutus.html')