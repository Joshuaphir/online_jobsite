
from django.db import models 
from users.models import User
from company.models import Company


#usage of textChoices

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100) 
    job_type = models.CharField(max_length=100) 
    requirements = models.TextField() 
    duties = models.TextField() 
    company_overview = models.TextField() 
    post_overview = models.TextField()
    edu_qualification = models.TextField(max_length=100)
    is_available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
#to be able to count applicant who applied a job we need this model
class AppliedJob(models.Model):
    status_choices = (('Received','Received'),
                      ('Declined','Declined'),
                      ('Pending','Pending'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True) 
    status = models.CharField(max_length=20, choices=status_choices) 