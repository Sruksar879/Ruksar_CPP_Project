from django.db import models
from django.contrib.auth.models import User

class Donor(models.Model):
    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

class BloodBag(models.Model):
    blood_group = models.CharField(max_length=10)
    volume = models.DecimalField(max_digits=5, decimal_places=2)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.blood_group} - {self.volume} mL"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username
