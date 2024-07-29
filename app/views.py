from django.shortcuts import render, redirect
from django.http import JsonResponse
from app.models import *
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import auth
from django.core.mail import EmailMessage
from email.message import EmailMessage
from django.conf import settings
from django.core.exceptions import ValidationError
# import smtplib

# Create your views here.
User = get_user_model()

def home(request):
    return render(request, "app/index.html")

def aboutus(request):
    return render(request, "app/about.html")

def event(request):
    return render(request, "app/event.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        messages = request.POST.get('message')
        body = f"Dear {name}, \nThank you for your message, we will get back to you soon. \n\nOderanti Funmilayo \nCEO of Summit Foundation"
        new_email = EmailMessage(subject ='Thank you for reaching out',
        body = body, from_email = settings.EMAIL_HOST_USER, to=[email])
        new_email.send()
        body2 = f"New contact message from{name}\n Email Address: {email}\n message:{messages}"
        another_email = EmailMessage(subject="New Contact Message",
        body = body2,
        from_email = settings.EMAIL_HOST_USER,
        to = [settings.EMAIL_HOST_USER])
        another_email.send()
    return render(request, "app/contact.html")
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     msg = EmailMessage()
    #     email_Address = 'EMAIL_HOST_USER'
    #     email_password = 'EMAIL_HOST_PASSWORD'
    #     msg.set_content(f"Dear {name}, \nThank you for your message, we will get back to you soon. \n\nOderanti Funmilayo \nCEO of Summit Foundation")
    #     msg["Subject"] = "Notification"
    #     msg['From'] = 'email'
    #     msg['To'] = 'EMAIL_HOST_USER'
    #     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    #         smtp.login(email_Address, email_password)
    #         smtp.send_message(msg)
    
def dashboard(request):
    products = Product.objects.all()
    context = {'products' :products}
    user = request.user
    if not user.is_authenticated:
        return redirect(login)
    return render(request, "app/dashboard.html", context)

def logout(request):
    auth.logout(request)
    return redirect(login)

def registeration(request):
    user = request.user
    if user.is_authenticated:
        return redirect(dashboard)
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        if not firstname:
            messages.error(request, 'First name is Compulsory')
            return render(request, "app/register.html")
        surname = request.POST.get('surname')
        if not surname:
            messages.error(request, 'Surname is Compulsory')
            return render(request, "app/register.html")
        username = request.POST.get('username')
        if not username:
            messages.error(request, 'Username is Compulsory')
            return render(request, "app/register.html")      
        password = request.POST.get("password")
        if len(password) < 8:
            messages.error(request, "Password must be up to 8 character")
            return render(request, "app/register.html")
        # if not re.search(r'[A-Z]', value):
        #     messages.error(request, 'Password must contain at least one uppercase letter.')
        #     return render(request, "app/register.html")
        # if not re.search(r'[a-z]', value):
        #     messages.error(request, 'Password must contain at least one lowercase letter.')
        #     return render(request, "app/register.html")
        # if not re.search(r'\d', value):
        #     messages.error(request, 'Password must contain at least one number.')
        #     return render(request, "app/register.html")
        cpassword = request.POST.get("cpassword")
        if password != cpassword:
            messages.error(request, "Password did not match")
            return render(request, "app/register.html")     
            
    
        username_already_taken = User.objects.filter(username=username).exists()
        if username_already_taken:
            messages.error(request, "Username already exist")
            return render(request, "app/register.html")
        
        new_user = User.objects.create(
            first_name = firstname,
            last_name = surname,
            username = username,            
        )
        new_user.set_password(password)
        new_user.save()
        messages.success(request, "Account created, please login")        
        return redirect(login)        
    return render(request, "app/register.html")

# def store(request):
#     context = {}
#     return render(request, "app/store.html", context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {'items' :items, 'order':order}
    return render(request, "app/cart.html", context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {'items' :items, 'order':order}
    return render(request, "app/checkout.html", context)

def login(request):
    user = request.user
    if user.is_authenticated:
        return redirect(dashboard)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        if not username or not password:
            messages.error(request, "Invalid details")
            return render(request, "app/login.html")
        user = auth.authenticate(username=username, password=password)
        if not user:
            messages.error(request, "Invalid login credentials")
            return render(request, "app/login.html")
        auth.login(request, user)
        return redirect(dashboard)
    return render(request, "app/login.html")

def discovermore(request):
    return render(request, "app/discover.html")

def updateItem(request):
    return JsonResponse('Item was added', safe=False)