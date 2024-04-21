from django.contrib import admin
from .models import User, AVDriver, AVStaff
# Register your models here.
admin.site.register(User)
admin.site.register(AVDriver)
admin.site.register(AVStaff)        