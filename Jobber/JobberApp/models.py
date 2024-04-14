from django.db import models

class UserDetails(models.Model):
    jobTitle = models.CharField(max_length=100)
    jobUrl = models.TextField()
    companyName = models.TextField()
    location = models.TextField()
    jobDescription = models.TextField()

    def __str__(self):
        return self.companyName  

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    company_description = models.TextField()

    def __str__(self):
        return self.company_name


class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=100)
    job_url = models.URLField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_location = models.CharField(max_length=100)
    job_description = models.TextField()

    def __str__(self):
        return self.job_title

class Applications(models.Model):
    application_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return f"Application {self.application_id}"