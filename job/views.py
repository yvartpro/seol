from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login,authenticate


# Create your views here
def register(request):
    if request.method=='POST':
       first_name=request.POST.get('first_name')
       last_name=request.POST.get('last_name')
       email=request.POST.get('email')
       address=request.POST.get('address')
       phone=request.POST.get('phone')
       type=request.POST.get('type')
       password=request.POST.get('password')
       password2=request.POST.get('password2')
       print(password2)
       if password != password2:
          context={
                  "sapor":"password not the same"
          }
          return render(request,'job/regigister.html',context)
       else:
           user=User.objects.create_user(username=email,email=email,password=password)
           user.first_name=first_name
           user.last_name=last_name
           user.address=address
           user.phone=phone
           user.type=type
           user.save()
           return redirect('login')
    return render(request,'job/register.html')
def signin(request):
    if request.method=='POST':
       email=request.POST.get('email')
       password=request.POST.get('password')

       user=authenticate(username=email,password=password)
       #print(user.type)
       if user is not None:
          login(request,user)
          if user.type == 'job_seeker':
             return redirect('profile')
          else:
             return redirect('dashboard')
       else:
            context={
            "sapor":"user is not none"
            }
       return render(request,'job/login.html',context)
    return render(request,'job/login.html')
def home(request):
    #print(request.user.first_name)
    post=Company_post.objects.all()
    seeker = People_post.objects.all()
    context = {
       'posts':post,
       'seekers':seeker,
    }
    return render(request,'job/index.html',context)

def dashboard(request):
    posts =  Company_post.objects.filter(user=request.user)
    try:
       img = Profile.objects.get(user=request.user)
       context = {
        'posts':posts,
        'img':img.photo,
       }
       return render(request,'job/dashboard.html',context)

    except:
      context = {
       'posts':posts,
     }
    return render(request,'job/dashboard.html',context)
def people_post(request):
    if request.method == 'POST':
       title = request.POST.get('title')
       description=request.POST.get('description')
       new = People_post(user=request.user,title=title,description=description)
       new.save()
    return redirect('profile')
#company post
def company_post(request):
    if request.method == 'POST':
       title = request.POST.get('title')
       photo=request.FILES.get('photo')
       deadline=request.POST.get('deadline')
       description=request.POST.get('description')
       new = Company_post(user=request.user,title=title,photo=photo,deadline=deadline,description=description)
       new.save()
    return  redirect('dashboard')

def profile(request):
    profile = People_profile.objects.filter(user=request.user)
    print(profile)
    try:
       img = Profile.objects.get(user=request.user)
       context = {
        'img':img.photo,
        'profile':profile,
       }
       if request.method == 'POST':
          title = request.POST.get('title')
          document=request.FILES.get('document')
          new = People_profile(user=request.user,title=title,document=document)
          new.save()
       return render(request,'job/profile.html',context)

    except:
       context = {
         'profile':profile,
       }
       if request.method == 'POST':
          title = request.POST.get('title')
          document=request.FILES.get('document')
          new = People_profile(user=request.user,title=title,document=document)
          new.save()
       return render(request,'job/profile.html',context)

def apply_job(request,post_id):
    post = Company_post.objects.get(id=post_id)
    new = Apply_job(user=request.user,post=post)
    new.save()
    return redirect('home')
def view_applicante(request,post_id):
    posts =  Company_post.objects.filter(user=request.user)
    candidate = Apply_job.objects.filter(post=post_id)
    context = {
     'posts':posts,
     'candidates':candidate,
     'view_profile':view_profile,
   }
    return render(request,'job/dashboard.html',context)

'''def post_expired(request):
    post = Company_post.objects.filter(expiry_date__gt=now())
    context = {
         'posts':post
    }
    return render(request,'job/index.html',context)'''

def view_profile(request,user_id):
    print(user_id)
    user = User.objects.get(id=user_id)
    print(user)
    profile = People_profile.objects.get(user=user)
    print(profile)
    try:
       img = Profile.objects.get(user=user)
       context = {
          'view_profile':profile,
          'img':img.photo,
          'user':user,
       }
       return render(request,'job/profile.html',context)

    except:
       context = {
          'view_profile':profile,
          'user':user,
       }
       return render(request,'job/profile.html',context)

def people_photo(request):
    if request.method == 'POST':
       foto = request.FILES.get('photo')
       try:
          new = Profile.objects.get(user=request.user)
          new.photo = foto
          new.save()
       except Exception as sapor:
         print(sapor)
         new = Profile(user=request.user,photo=foto)
         new.save()
    if request.user.type == "job_seeker":
       return redirect('profile')
    else:
       return redirect('dashboard')
