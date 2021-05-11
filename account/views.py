from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

#회원가입
def signup(request):
    if request.method == 'POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])  
                auth.login(request, user)
                return redirect('main')
        else:
            return render(request, 'accounts/signup.html',{'error':'Passwords must match'})
    else: 
        return render(request, 'accounts/signup.html')

#로그인
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request,'accounts/login.html',{'error':'username or password is incorrect'})
    else:
        return render(request, 'accounts/login.html')

#로그아웃
def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('main')
    return render(request,'accounts/signup.html')

#마이페이지
def mypage(request):
    return render(request,'accounts/mypage.html')

#마이페이지 내 회원탈퇴
def mem_delete(request):
    request.user.delete()
    return redirect('home')