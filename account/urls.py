from django.urls import path
from .views import (
    home,
    register_view,
    login_view,
    logout_view,
    dashboard,
    cancel_appointment,
    about,
    doctors,
    contact
)

urlpatterns = [
    path('', home, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('cancel/<int:id>/', cancel_appointment, name='cancel_appointment'),
    
    path('about/', about, name='about'),
    path('doctors/', doctors, name='doctors'),
    path('contact/', contact, name='contact'),
]