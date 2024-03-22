from django.db import models

class UserDetails(models.Model):
    jobTitle = models.CharField(max_length=100)
    jobUrl = models.TextField()
    companyName = models.TextField()
    location = models.TextField()
    jobDescription = models.TextField()

    def __str__(self):
        return self.name  
