from django.shortcuts import render
from Main.models import feedback_msg
# Create your views here.
from django.core.mail import send_mail
from django.conf import settings



def send_connec_us(email,first_name,last_name,country,msg):
    subject = f'{first_name} {last_name} from {country}'
    email_from = settings.EMAIL_HOST_USER
    message = msg

    send_mail(subject,message,email_from,[email])

def home(request):
    return render(request,'index.html')

def user_login(request):
    return render(request,'login.html')


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

