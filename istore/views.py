from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,auth
from istore.models import Contact,salesdetails,productsdetails
from datetime import datetime
from django.contrib import messages

# Create your views here.
def home(request):
    
    return render(request,'home.html')

def products(request):
    if request.user.is_anonymous:
        return redirect('log_in')
    
    
    prod=productsdetails.objects.all()
    return render(request,'products.html',{'prod':prod})

def feedback(request):
    if request.method == "POST":
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        feedback=request.POST['feedback']
        contact=(Contact(name=name, phone=phone, email=email, feedback=feedback, date=datetime.today()))
        contact.save()
        messages.success(request,"Your message is been sent !")
        
    return render(request,'feedback.html')

def logIn(request):
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        User=authenticate(username=loginusername,password=loginpassword)
        if User is not None:
            login(request,User)
            messages.success(request,"Your have been logged IN  !")
            return redirect('home')

    return render(request,'login.html')

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1=request.POST['password1']
        password2=request.POST['password2']


        if password1 != password2:
            messages.warning(request,"Password do not match!")
            return redirect('sign_up')
        else:
            my_user=User.objects.create_user(username,email,password1)
            my_user.last_name=last_name
            my_user.first_name=first_name
            my_user.save()
            messages.success(request,"Your account has been created !")
            return redirect('log_in')
        
       
    return render(request,'sign_up.html')

def logout(request):
    auth.logout(request)
    messages.success(request,"Your have been logged out !")
    return redirect('home')

def sales_book(request):
    
    if request.method=="POST":
        print(request.POST)
        print("------------------------")
        coustmername=request.POST['coustmername']
        phonenumber=request.POST['phonenumber']
        secondaryphonenumber=request.POST['secondaryphonenumber']
        productname=request.POST['productname']
        quantity=request.POST['quantity']
        deliveryaddress=request.POST['deliveryaddress']
        pincode=request.POST['pincode']
        sales_details=salesdetails(coustmername=coustmername, phonenumber=phonenumber, secondaryphonenumber=secondaryphonenumber,productname=productname,quantity=quantity,deliveryaddress=deliveryaddress,pincode=pincode,date=datetime.today() )
        
        data_quantity=productsdetails.objects.filter(prod_name=productname).get()
        dataquantity=int(data_quantity.prod_quantity) 
        orderquantity=int(quantity)
        if dataquantity<orderquantity:
            messages.error(request,"plz enter right amount of quantity !")
        else:
            updatequantity=dataquantity-orderquantity
            productsdetails.objects.filter(prod_name=productname).update(prod_quantity=updatequantity)
            sales_details.save()
            messages.success(request,"Your's Order has been placed !")


    return render(request,'sales.html')   
        

            
         
    

   



   
