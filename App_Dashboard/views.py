from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from App_Dashboard import forms
from App_Dashboard.models import Country, TaxiCompany


@login_required
def home(request):
    country_list = Country.objects.all()
    users = User.objects.all()
    taxi_companies = TaxiCompany.objects.all()
    diction = {
        'title': 'Dashboard',
        'country_list': country_list,
        'users': users,
        'taxi_companies': taxi_companies
    }
    return render(request, "App_Dashboard/home.html", context=diction)

@login_required
def country(request):
    country_list = Country.objects.all()
    diction = {
        'title': 'Country_List',
        'country_list': country_list
    }
    return render(request, "App_Dashboard/country.html", context=diction)

@login_required
def country_form(request):
    form = forms.CountryForm()

    if request.method == 'POST':
        form = forms.CountryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Country Added Successfully')
            return HttpResponseRedirect(reverse('App_Dashboard:country'))
    diction = {
        'title': "Add Country",
        'country_form': form
    }
    return render(request, "App_Dashboard/country_form.html", context=diction)

@login_required
def edit_country(request, country_id):
    country_info = Country.objects.get(pk=country_id)
    form = forms.CountryForm(instance=country_info)

    if request.method == 'POST':
        form = forms.CountryForm(request.POST, instance=country_info)

        if form.is_valid():
            form.save(commit=True)
            messages.info(request, 'Country Updated Successfully')
            return HttpResponseRedirect(reverse('App_Dashboard:country'))
    diction = {
        'edit_form': form
    }
    return render(request, 'App_Dashboard/edit_country.html', context=diction)

@login_required
def delete_country(request, country_id):
    Country.objects.get(pk=country_id).delete()
    messages.success(request, 'Country Deleted Successfully')
    return HttpResponseRedirect(reverse('App_Dashboard:country'))

@login_required
def taxi_company(request):
    taxi_companies = TaxiCompany.objects.all()
    print(taxi_companies)
    diction = {
        'title': 'Taxi Company',
        'taxi_companies': taxi_companies,
    }
    return render(request, "App_Dashboard/taxi_company_list.html", context=diction)

@login_required
def add_taxi_company(request):
    form = forms.TaxiCompanyForm()

    if request.method == 'POST':
        form = forms.TaxiCompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Taxi Company Added Successfully')
            return HttpResponseRedirect(reverse('App_Dashboard:taxi_company'))
    diction = {
        'title': "Add Taxi Company",
        'taxi_form': form
    }
    return render(request, "App_Dashboard/taxi_company_form.html", context=diction)

@login_required
def edit_taxi_company(request, taxi_id):
    taxi_info = TaxiCompany.objects.get(pk=taxi_id)
    form = forms.TaxiCompanyForm(instance=taxi_info)

    if request.method == 'POST':
        form = forms.TaxiCompanyForm(request.POST, request.FILES, instance=taxi_info)

        if form.is_valid():
            form.save(commit=True)
            messages.info(request, 'Taxi Company Updated Successfully')
            return HttpResponseRedirect(reverse('App_Dashboard:taxi_company'))
    diction = {
        'edit_form': form
    }
    return render(request, 'App_Dashboard/edit_taxi_company.html', context=diction)

@login_required
def delete_taxi_company(request, taxi_id):
    TaxiCompany.objects.get(pk=taxi_id).delete()
    messages.success(request, 'Taxi Company Deleted Successfully')
    return HttpResponseRedirect(reverse('App_Dashboard:taxi_company'))