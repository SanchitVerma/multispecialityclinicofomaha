
from django.db import models

# Create your models here.


class Customers(models.Model):
    cust_name = models.CharField(max_length=50)
    insurance_number = models.CharField(max_length=6, blank=False, null=False)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=50)
    dob = models.DateTimeField(null=False)
    address = models.CharField(max_length=200)

    def __str__(self):
        return str(self.cust_name)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


class Providers(models.Model):
    provider_name = models.CharField(max_length=50)
    provider_id = models.CharField(max_length=5, blank=False, null=False)
    speciality = models.CharField(max_length=100)

    def __str__(self):
        return str(self.provider_name + self.provider_id)

    class Meta:
        verbose_name = "Provider"
        verbose_name_plural = "Providers"


class Claims(models.Model):
    claim_number = models.IntegerField(blank=False, null=False)
    provider_name = models.ForeignKey(Providers, on_delete=models.CASCADE, related_name='a')
    #provider_id = models.ForeignKey(Providers, on_delete=models.CASCADE, related_name='b')
    cust_name = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name='c')
    insurance_number = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name='d')
    claim_date = models.DateTimeField()
    claim_amount = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return str(self.claim_number)

    class Meta:
        verbose_name = "Claim"
        verbose_name_plural = "Claims"
