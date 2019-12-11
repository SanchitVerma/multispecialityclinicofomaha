from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [

    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/create', views.customer_new, name='customer_new'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('provider_list', views.provider_list, name='provider_list'),
    path('provider/create', views.provider_new, name='provider_new'),
    path('provider/<int:pk>/edit/', views.provider_edit, name='provider_edit'),
    path('provider/<int:pk>/delete/', views.provider_delete, name='provider_delete'),
    path('claim_list', views.claim_list, name='claim_list'),
    path('claim/create', views.claim_new, name='claim_new'),
    path('claim/<int:pk>/edit/', views.claim_edit, name='claim_edit'),
    path('claim/<int:pk>/delete/', views.claim_delete, name='claim_delete'),
    path('appointment_list', views.appointment_list, name='appointment_list'),
    path('appointment/create', views.appointment_new, name='appointment_new'),
    path('appointment/<int:pk>/edit/', views.appointment_edit, name='appointment_edit'),
    path('appointment/<int:pk>/delete/', views.appointment_delete, name='appointment_delete'),
]
