from django.contrib import admin
from .models import Doctor, Appointment, ContactMessage

admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(ContactMessage)