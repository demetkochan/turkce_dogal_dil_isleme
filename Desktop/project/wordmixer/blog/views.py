
from django.db.models import fields
from .models import FileUpload
from .forms import UploadFileForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth



def index(request):
    if request.method == "POST":
        if request.POST.get('submit') == 'Kayıt Ol':
            username= request.POST['username']
            email= request.POST['email']
            password= request.POST['password']

            if User.objects.filter(username=username).exists():
               messages.info(request,'Bu kullanıcı adı kullanılıyor')
               return redirect('/')
            elif User.objects.filter(email=email).exists():
               messages.info(request,'Bu email kullanılıyor.')
               return redirect('/')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('/')

        elif request.POST.get('submit') == 'Oturum Aç':
            username= request.POST.get('username')
            password= request.POST.get('password')

            user= auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('/anasayfa')
            else : 
                messages.info(request,'Yanlış kullanıcı adı veya şifre')
                return redirect('/')

    else:
        return render(request, 'blog/SignPage.html')
    
def home(request):
    return render (request,'blog/HomePage.html')

def logout (request):
    auth.logut(request)
    return redirect('/')

def link1(request):
    if request.method == "POST":
        uf=UploadFileForm(request.POST,request.FILES)
        if uf.is_valid():
            uf = FileUpload(file = request.FILES['file'])
            uf.user = request.user
            uf.save()
            return redirect('/duyguanalizi')
        else:
            uf=UploadFileForm()
        return render (request,'blog/links/Link1.html',{'uf': uf})

    elif request.POST.get('submit') == 'Dene':
        text = request.POST['text']
        text = request.POST.get('text')
        return redirect('/duyguanalizi')
    else :
        return render (request,'blog/links/Link1.html')



    
def link2(request):
    return render (request,'blog/links/Link2.html')
def link3(request):
    return render (request,'blog/links/Link3.html')
def link4(request):
    return render (request,'blog/links/Link4.html')
def link5(request):
    return render (request,'blog/links/Link5.html')
def link6(request):
    return render (request,'blog/links/Link6.html')





 