from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    AV_STAFF = 'staff'
    AV_DRIVER = 'driver'
    USER_TYPE_CHOICES = [
        (AV_STAFF, 'AV Service Cloud Staff'),
        (AV_DRIVER, 'AV Driver'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default=AV_STAFF)

class AVDriver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=255)
    vehicle_color = models.CharField(max_length=50)
    model_number = models.CharField(max_length=100)
    sensor_info = models.TextField()

class AVStaff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


