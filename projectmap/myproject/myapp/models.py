from django.db import models

# Create your models here.
class book(models.Model):
    titie=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    pdf=models.FileField(upload_to='book/pdf')
    cover=models.ImageField(upload_to='book/cover')