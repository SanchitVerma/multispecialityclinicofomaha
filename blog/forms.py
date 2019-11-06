from django import forms
from .models import Customers, Providers, Claims, Appointments


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ('cust_name', 'insurance_number', 'email', 'phone_number', 'dob', 'address')


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Providers
        fields = ('provider_name', 'provider_id', 'speciality')


class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claims
        fields = ('claim_number', 'provider_id', 'insurance_number', 'claim_date', 'claim_amount')


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ('appointment_number', 'provider_id', 'insurance_number', 'appointment_date', 'appointment_time')