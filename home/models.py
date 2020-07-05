from django.db import models

# Create your models here.
class Quote(models.Model):
    name = models.CharField(max_length=30,null=True,blank=True)
    email = models.EmailField(null=False,blank=False)
    message = models.TextField(null=False,blank=False)
    date = models.DateTimeField(auto_now_add=True)
    