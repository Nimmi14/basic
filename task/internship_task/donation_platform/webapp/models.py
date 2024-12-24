
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Donar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username=models.CharField(max_length=100, default="default_username" ,unique=True)
    email = models.EmailField()
    password1= models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    # profile = models.FileField(upload_to='patient_pics/')

# Create your models here.
    def __str__(self):
        return self.username