from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.core.mail import send_mail


def home(request):
    return render(request, 'blog/home.html',
                  {'blog': home})


@login_required
def customer_list(request):
    customer = Customers.objects.all()
    return render(request, 'blog/customer_list.html', {'Customers': customer})


@login_required
def customer_new(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            customer = Customers.objects.all()
            return render(request, 'blog/customer_list.html',
                          {'customers': customer})
    else:
        form = CustomerForm()
    send_mail('Hello Customer',
              'You are now registered as a customer with the Multi-speciality Clinic Of Omaha',
              'sanchitverma2691@gmail.com', ['7784de963-d08f45@inbox.mailtrap.io'], fail_silently=False)
    return render(request, 'blog/customer_new.html', {'form': form})


@login_required
def customer_edit(request, pk):
    customer = get_object_or_404(Customers, pk=pk)
    if request.method == "POST":
        # update
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return render(request, 'blog/customer_list.html',
                          {'customers': customer})
    else:
        # edit
        form = CustomerForm(instance=customer)
    return render(request, 'blog/customer_edit.html', {'form': form})


@login_required
def customer_delete(request, pk):
    customer = get_object_or_404(Customers, pk=pk)
    customer.delete()
    return redirect('blog:customer_list')


@login_required
def provider_list(request):
    provider = Providers.objects.all()
    return render(request, 'blog/provider_list.html', {'Providers': provider})


@login_required
def claim_list(request):
    claim = Claims.objects.all()
    return render(request, 'blog/claim_list.html', {'Claims': claim})


@login_required
def claim_new(request):
    if request.method == "POST":
        form = ClaimForm(request.POST)
        if form.is_valid():
            claim = form.save(commit=False)
            claim.save()
            claim = Claims.objects.all()
            return render(request, 'blog/claim_list.html',
                          {'claims': claim})
    else:
        form = ClaimForm()
    return render(request, 'blog/claim_new.html', {'form': form})


@login_required
def claim_edit(request, pk):
    claim = get_object_or_404(Claims, pk=pk)
    if request.method == "POST":
        # update
        form = ClaimForm(request.POST, instance=claim)
        if form.is_valid():
            claim = form.save(commit=False)
            claim.save()
            return render(request, 'blog/claim_list.html',
                          {'claims': claim})
    else:
        # edit
        form = ClaimForm(instance=claim)
    return render(request, 'blog/claim_edit.html', {'form': form})


@login_required
def claim_delete(request, pk):
    claim = get_object_or_404(Claims, pk=pk)
    claim.delete()
    return redirect('blog:claim_list')
