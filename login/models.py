from django.db import models

# Create your models here.
    
class logindata(models.Model):
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    date=models.DateField()
    
    def __str__(self):
        return self.email