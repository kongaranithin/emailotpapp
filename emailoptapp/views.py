from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import random
class Home(View):
    def get(self, request):
        return render(request,'input.html')
class SendMail(View):
    def get(self, request):
        otp=(random.randint(000000,999999))
        print(otp)
        From_Email=settings.EMAIL_HOST_USER
        email=request.GET['t1']
        to_list=[email]
        send_mail(otp,From_Email,email,to_list,fail_silently=False)
        return HttpResponse("sent otp successfully")





# Create your views here.
