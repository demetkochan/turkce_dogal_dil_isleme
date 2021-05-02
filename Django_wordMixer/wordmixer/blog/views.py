
from django.db.models import fields
from .models import FileUpload
from .forms import UploadFileForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
import requests
from django.http import JsonResponse
import json 

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
                messages.info(request,'Kayıt olundu! Giriş yapabilirsiniz. ')
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
    auth.logout(request)
    return redirect('/')

def link1(request):
    if request.method == "POST":
        uf=UploadFileForm(request.POST,request.FILES)
        if uf.is_valid():
            uf = FileUpload(file = request.FILES['file'])
            uf.user = request.user
            uf.save()
    else:
        uf=UploadFileForm()
    return render (request,'blog/links/Link1.html',{'uf': uf})

def sentiment(request):
    url =  "http://localhost:1000/sentiment"
    payload = {"text": request.POST["input_text"]}
    response = json.loads(requests.request("POST", url, json=payload).text)
    return render (request,'blog/links/Link1.html',{'response': response} )

def link2(request):
    return render (request,'blog/links/Link2.html')

def keywordExtraction(request):
    url =  "http://localhost:2000/keyword"
    text= request.POST["input_text"] 
    key_number= request.POST["key_number"]
    payload = {"text":text, "key_number":key_number}
    response = json.loads(requests.request("POST", url, json=payload ).text)
    return render (request,'blog/links/Link2.html',{'response': response} )

def link3(request):
    return render (request,'blog/links/Link3.html')

def summarization(request):
    url =  "http://localhost:3000/summarization"
    payload = {"text": request.POST["input_text"]}
    response = json.loads(requests.request("POST", url, json=payload).text)
    return render (request,'blog/links/Link3.html',{'response': response} )

def link4(request):
    return render (request,'blog/links/Link4.html')

def ner(request):
    url =  "http://localhost:4000/ner"
    payload = {"text": request.POST["input_text"]}
    response = json.loads(requests.request("POST", url, json=payload).text)
    return render (request,'blog/links/Link4.html',{'response': response} ) 

def link5(request):
    return render (request,'blog/links/Link5.html')

def questionAnswer(request): 
        url =  "http://localhost:5000/questionAns"   
        text= request.POST["input_text"] 
        question= request.POST["question"]
        payload = {"text":text, "question":question} 
        response = json.loads(requests.request("POST", url, json=payload).text)
        return render (request,'blog/links/Link5.html',{'response': response} )

def link6(request):
    return render (request,'blog/links/Link6.html')

def categorization(request):
    url =  "http://localhost:6000/categorize"
    payload = {"text": request.POST["input_text"]}
    response = json.loads (requests.request("POST", url, json=payload).text)
    return render (request,'blog/links/Link6.html',{'response': response} )





 