from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import  *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
def base(request):
    return render(request, 'base.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user=User.objects.get(user)
            request.session['user_id'] = user.id
        except:
            messages.error(request,"user not exist")
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect ('details')
        
    return render(request, 'login.html')

def logoutpage(request):
    logout(request)
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('base')



def registerpage(request):
    form=UserCreationForm()
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            request.session['user_id'] = user.id
            return redirect('details')
        else:
            messages.error(request,"error accurred in registration")
            
    return render(request,'register.html',{'form':form})


@login_required
def edit_bio_data(request):
    # user_id = request.session.get('user_id')
    # if not user_id:
    #     return redirect('loginpage')

    user=request.user.id

    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        date_of_birth = request.POST['date_of_birth']
        gender = request.POST['gender']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        qualification = request.POST['qualification']
        occupation = request.POST['occupation']

        obj=BioData.objects.create(user_id=user,name=name, age=age, date_of_birth=date_of_birth, gender=gender, phone_number=phone_number, email=email, qualification=qualification, occupation=occupation)
        obj.save()
        return redirect('bio_data')
    
    return render(request, 'enter_bio_data.html')

@login_required
def bio_data(request):
    # user_id = request.session.get('user_id')
    # if not user_id:
    #     return redirect('loginpage')
    
    user=request.user
    bio_data = BioData.objects.filter(user_id=user)
    return render(request, 'show_bio_data.html', {'bio_data':bio_data})



def viewpage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    biodata = BioData.objects.filter(Q(name__icontains=q)|
                                     Q(age__icontains=q) | 
                                     Q(date_of_birth__icontains=q)
                                     )
    return render(request,"details.html",{'biodata':biodata})


@login_required
def userdetails(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        date_of_birth = request.POST['date_of_birth']

        userid=request.user.id
        print(userid)
        obj=detailspage.objects.create(details_id=userid,name=name, age=age, date_of_birth=date_of_birth)
        obj.save()
        return redirect('showuser')
    return render(request,'user.html')
 
def showuser(request):
    userid=request.user.id
    user_details = detailspage.objects.filter(details_id=userid)

    return render(request,'showuser.html',{'user_details':user_details})

def delete_user(request,id):
    if request.user.is_authenticated:
        deleteid=BioData.objects.filter(id=id)
        deleteid.delete()
    return redirect('bio_data')

def update_user(request,id):
    if request.user.is_authenticated:
        try:
            biodata=BioData.objects.get(id=id)

            if request.method == 'POST':
                    biodata.name = request.POST.get('name')
                    biodata.age = request.POST.get('age')
                    biodata.date_of_birth = request.POST.get('date_of_birth')
                    biodata.gender = request.POST.get('gender')
                    biodata.phone_number = request.POST.get('phone_number')
                    biodata.email = request.POST.get('email')
                    biodata.qualification = request.POST.get('qualification')
                    biodata.occupation = request.POST.get('occupation')
                    biodata.save()
                    return redirect('bio_data')
            return render(request,'update.html',{'biodata':biodata})
            
        except BioData.DoesNotExist:
            return redirect('bio_data')
    
    return render(request,'update.html',{'biodata':biodata})
