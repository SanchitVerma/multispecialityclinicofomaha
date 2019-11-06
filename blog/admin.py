from django.contrib import admin
from .models import Customers, Providers, Claims, Appointments


class CustomersList(admin.ModelAdmin):
    list_display = ('cust_name', 'insurance_number', 'email', 'phone_number', 'dob', 'address')
    list_filter = ('cust_name', 'insurance_number')
    search_fields = ('cust_name', 'insurance_number')
    ordering = ['cust_name']


class ProvidersList(admin.ModelAdmin):
    list_display = ('provider_name', 'provider_id', 'speciality')
    list_filter = ('provider_name', 'provider_id')
    search_fields = ('provider_name', 'provider_id')
    ordering = ['provider_name']


class ClaimsList(admin.ModelAdmin):
    list_display = ('claim_number', 'provider_id', 'insurance_number', 'claim_date', 'claim_amount')
    list_filter = ('claim_number', 'provider_id', 'insurance_number')
    search_fields = ('claim_number', 'provider_id', 'insurance_number')
    ordering = ['claim_number']


class AppointmentList(admin.ModelAdmin):
    list_display = ('appointment_number', 'provider_id', 'insurance_number', 'appointment_date', 'appointment_time')
    list_filter = ('appointment_number', 'provider_id', 'insurance_number')
    search_fields = ('appointment_number', 'provider_id', 'insurance_number')
    ordering = ['appointment_number']


admin.site.register(Customers, CustomersList)
admin.site.register(Providers, ProvidersList)
admin.site.register(Claims, ClaimsList)
admin.site.register(Appointments, AppointmentList)
