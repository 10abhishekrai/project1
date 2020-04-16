from django.db import models

# Create your models here.
class student(models.Model):
    student_id = models.AutoField
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    ph_number = models.IntegerField(max_length=12)
    image = models.ImageField(upload_to='pics')
    status = models.BooleanField()