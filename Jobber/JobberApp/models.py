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
    job_title = models.CharField(max_length=100, null=True)
    job_URL = models.CharField(max_length=255,null=True)
    company = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True)
    max_salary = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    min_salary = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    location = models.CharField(max_length=100, null=True)
    date_applied = models.DateField(default='2024-10-20', null=True)
    follow_up_date = models.DateField(blank=True, default='2024-10-20', null=True)
    notes = models.TextField(blank=True, null=True)
    job_description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'applications'

class Contacts(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    company = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    link = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'contacts'