from django.db import models

# Create your models here.
class Account(models.Model):
    mobile = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    owner = models.CharField(max_length=20)

    def __str__(self):
        return self.mobile