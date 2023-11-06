from django.db import models

# Create your models here.

class Sign(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.IntegerField()
    confirmpassword = models.IntegerField()

    def __str__(self):
        return self.username
    
class Log(models.Model):
    email = models.EmailField()
    password = models.IntegerField()


    def __str__(self):
        return self.email
