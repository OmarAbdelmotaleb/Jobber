from django.db import models

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'users'

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    company_description = models.TextField()

    class Meta:
        db_table = 'company'

class Applications(models.Model):
    application_id = models.AutoField(primary_key=True)

    user = models.ForeignKey('Users', models.DO_NOTHING)
    job_title = models.CharField(max_length=100)
    job_URL = models.CharField(max_length=255)
    company = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    max_salary = models.DecimalField(max_digits=10, decimal_places=0)
    min_salary = models.DecimalField(max_digits=10, decimal_places=0)
    location = models.CharField(max_length=100)
    date_applied = models.DateField()
    follow_up_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)
    job_description = models.TextField(blank=True)

    class Meta:
        db_table = 'applications'