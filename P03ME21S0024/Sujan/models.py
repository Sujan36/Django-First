from django.db import models

# Create your models here.
class sujan_details(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=40,primary_key=True)
    password=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    qualification=models.CharField(max_length=20)
    ambitions=models.CharField(max_length=20)
    hobbies=models.CharField(max_length=20)

