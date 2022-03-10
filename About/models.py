from xml.parsers.expat import model
from django.db import models

# Create your models here.
class About(models.Model):
    company_name = models.CharField(max_length=100)
    description = models.TextField()
    oppaning_date = models.DateField()
    image = models.ImageField(upload_to='about/')
