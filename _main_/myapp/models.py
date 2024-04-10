from django.db import models

class Applications(models.Model):
    application_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    job = models.ForeignKey('Job', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'applications'

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    company_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=100)
    job_url = models.CharField(max_length=255)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    job_location = models.CharField(max_length=100, blank=True, null=True)
    job_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'