
from django.db import models 
from users.models import User

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100, null=True, blank=True) 
    est_date = models.PositiveIntegerField(null=True, blank=True) 
    district = models.CharField(max_length=100, null=True, blank=True) 
    headQuaters = models.CharField(max_length=100, null=True, blank=True) 
    region = models.CharField(max_length=100, null=True, blank=True)
    
    def _str_(self):
        return self.name