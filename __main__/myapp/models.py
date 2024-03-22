from django.db import models

class UserDetails(models.Model):
    name = models.CharField(max_length=100)
    degree = models.TextField()
    jobProfile = models.TextField()
    schoolName = models.TextField()

    def __str__(self):
        return self.name  
