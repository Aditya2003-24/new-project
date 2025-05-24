from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.
def landing(request):
    return render(request,'landing.html')
def addmin(request):
     adminname='admin@gmail.com'
     return render(request,'admin.html',{'admindata':adminname})
def login(request):
    email=request.POST.get('email')
    passw=request.POST.get('password')
    
    if request.method=='POST':
        adminname='admin@gmail.com'
        adminpass='2040'

        if email==adminname and passw==adminpass:
            return render(request,'admin.html',{'admindata':adminname})
        
    if request.method=='POST':

            user=Employee.objects.get(emp_email=email)
            if user:
                
                userdata=Employee.objects.get(emp_email=email)
                pass2=userdata.emp_password
                print(userdata.emp_password)
                print(userdata)
                print(passw)

                if str(passw).strip() == str(pass2).strip():

                    print('helo')
                    return render(request,'employee.html',{'userdata':userdata})
                

                
                
    else:
        return render(request,'login.html')
    
def register(request):
    adminname='admin@gmail.com'
    aditya='admin aditya yadav'
    if request.method=='POST':
        if request.method=='POST':
  
           username=request.POST.get('empName')
           email=request.POST.get('email')
           department=request.POST.get('department')
           phone=request.POST.get('contact')
           age=request.POST.get('age')
           joinDate=request.POST.get('joinDate')
           image=request.FILES.get('file')
           password=request.POST.get('password')
         
   

           u=Employee.objects.filter(emp_email=email)
           if u:
               msg='Email already exist'
               return render(request,'admin.html',{'key':msg,'admindata':adminname,'aditya':aditya})
           else:
             if password==password:
               Employee.objects.create(emp_name=username,emp_email=email,emp_Joining=joinDate,emp_dep=department,emp_contact=phone,emp_age=age,emp_image=image,emp_password=password)
               msg='registration done'
               return render(request,'admin.html',{'key':msg,'admindata':adminname,'aditya':aditya})
             else:
                msg1='pssword and cpssword not match'
                return render(request,'admin.html',{'key':msg1,'admindata':adminname,'aditya':aditya})
         
    else:
         return render(request,'admin.html',{'admindata':adminname,'aditya':aditya}) 
def alldata(request):
    data=Employee.objects.all()
    adminname='admin@gmail.com'
    return render(request,'admin.html',{'data':data,'admindata':adminname})

def editdata(request,pk):
    adminname='admin@gmail.com'
    data=Employee.objects.all()
    editdata=Employee.objects.get(id=pk)
    return render(request,'admin.html',{'editdata':editdata,'admindata':adminname,'data':data})

def edit(request,pk):
    username=request.POST.get('empName')
    email=request.POST.get('email')
    department=request.POST.get('department')
    phone=request.POST.get('contact')
    age=request.POST.get('age')
    joinDate=request.POST.get('joinDate')
           
    if request.method=='POST':
        edit=Employee.objects.get(id=pk)
        edit.emp_name=username
        edit.emp_email=email
        edit.emp_Joining=joinDate
        edit.emp_dep=department
        edit.emp_contact=phone
        edit.emp_age=age
        edit.save()
        adminname='admin@gmail.com'
        data=Employee.objects.all()
        return render(request,'admin.html',{'admindata':adminname,'data':data})
    
def delete(request,pk):
    delet=Employee.objects.get(id=pk)
    delet.delete()
    adminname='admin@gmail.com'
    data=Employee.objects.all()
    return render(request,'admin.html',{'admindata':adminname,'data':data})

        
def profile(request,pk):
    userdata=Employee.objects.get(id=pk)
    return render(request,'profile.html',{'userdata':userdata})

def search(request):
    
    x=request.POST.get('name')
    b=request.POST.get('age')
    c=request.POST.get('contact')
    d=request.POST.get('department')
    e=request.POST.get('email')
    print(x)
    searchdata=Employee.objects.filter(Q(emp_name__icontains=x) | Q(emp_email__icontains=e) | Q(emp_dep__icontains=d) | Q(emp_contact__icontains=c) | Q(emp_age__icontains=b))
    print(searchdata)
    adminname='admin@gmail.com'
    return render(request,'admin.html',{'data':searchdata,'admindata':adminname})