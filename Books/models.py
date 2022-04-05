from django.db import models

# Create your models here.
class Add_Book_detail(models.Model):
    Name = models.CharField(max_length=100)
    Author_Name = models.CharField(max_length=100)
    Publish_date = models.DateField()
    Price = models.IntegerField()