from django.db import models

class Form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    occupation = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"