from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib import admin


# Create your models here.

class Customers(models.Model):
    cust_name = models.CharField(max_length=50)
    insurance_number = models.CharField(primary_key=True, max_length=6, blank=False, null=False)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=50)
    dob = models.DateTimeField(null=False)
    address = models.CharField(max_length=200)

    def __str__(self):
        return str(self.insurance_number)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


class Providers(models.Model):
    provider_name = models.CharField(max_length=50)
    provider_id = models.CharField(primary_key=True, max_length=5, blank=False, null=False)
    speciality = models.CharField(max_length=100)

    def __str__(self):
        return str(self.provider_id)

    class Meta:
        verbose_name = "Provider"
        verbose_name_plural = "Providers"


class Claims(models.Model):
    claim_number = models.IntegerField(primary_key=True, blank=False, null=False)
    provider_id = models.ForeignKey(Providers, on_delete=models.CASCADE, related_name='b')
    insurance_number = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name='d')
    claim_date = models.DateTimeField()
    claim_amount = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return str(self.claim_number)

    class Meta:
        verbose_name = "Claim"
        verbose_name_plural = "Claims"


class Appointments(models.Model):
    appointment_number = models.IntegerField(primary_key=True, blank=False, null=False)
    provider_id = models.ForeignKey(Providers, on_delete=models.CASCADE, related_name='a')
    insurance_number = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name='b')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    def __str__(self):
        return str(self.appointment_number)

    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"
