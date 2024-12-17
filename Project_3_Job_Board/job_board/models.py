from django.db import models

# Create your models here.
# model represents a table in the db
# Attributes are fields in the table

class JobPosting(models.Model):
    # id starts at 1 and auto increments
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    is_active = models.BooleanField(default=False)
    

# makemigrations
# -> creates instructions telling django how the db has changed
# migrate
# -> applies the changes

