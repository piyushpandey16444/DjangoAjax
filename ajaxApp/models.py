from django.db import models

# Create your models here.
class Office(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    


class Employee(models.Model):
    GENDER = (
        ('female', "Female"),
        ('male', "Male"),
    )
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    gender = models.CharField(max_length=50, choices=GENDER)
    office = models.ForeignKey("ajaxApp.Office", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
