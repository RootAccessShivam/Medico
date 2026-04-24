from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor, Appointment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    doctors = Doctor.objects.all()

    if request.method == "POST":

        # 🔐 Prevent booking without login
        if not request.user.is_authenticated:
            return redirect('login')

        doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')

        if doctor_id and date:
            doctor = Doctor.objects.get(id=doctor_id)

            Appointment.objects.create(
                user=request.user,
                doctor=doctor,
                date=date
            )

        return render(request, 'home.html', {
            'doctors': doctors,
            'success': True
        })

    return render(request, 'home.html', {'doctors': doctors})


@login_required
def dashboard(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'appointments': appointments})


# 🔐 REGISTER
from django.contrib import messages

from django.contrib import messages
from django.contrib.auth.models import User

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username or not password:
            messages.error(request, "All fields are required!")
            return redirect('register')
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')  
        
        user = User.objects.create_user(username=username, password=password)

        messages.success(request, "Account created successfully!")

        # 🔁 Redirect to dashboard (or home)
        return redirect('home')   # you can change to 'home'


    return render(request, 'register.html')
# 🔐 LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


# 🔐 LOGOUT
def logout_view(request):
    logout(request)
    return redirect('home')

from django.shortcuts import get_object_or_404

@login_required
def cancel_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id, user=request.user)
    appointment.delete()
    return redirect('dashboard')

def about(request):
    return render(request, 'about.html')

def doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctors': doctors})

def contact(request):
    return render(request, 'contact.html')
from .models import ContactMessage
from django.contrib import messages

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_text = request.POST.get('message')

        if name and email and subject and message_text:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_text
            )
            messages.success(request, "Message sent successfully!")
        else:
            messages.error(request, "All fields are required!")

    return render(request, 'contact.html')