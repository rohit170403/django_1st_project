from django.db import models

class Contact(models.Model):
    email = models.EmailField()
    passw =models.CharField(max_length = 122)
    addr = models.CharField(max_length = 122)
    city = models.CharField(max_length = 122)
    state = models.CharField(max_length = 122)
    zip = models.CharField(max_length = 122)
    date=models.DateField()

    def __str__(self):
        return self.email

# Create your models here.

