from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from App_Dashboard import forms
from App_Dashboard.models import Country


@login_required
def home(request):
    country_list = Country.objects.all()
    users = User.objects.all()
    diction = {
        'title': 'Dashboard',
        'country_list': country_list,
        'users': users
    }
    return render(request, "App_Dashboard/home.html", context=diction)


def country(request):
    country_list = Country.objects.all()
    diction = {
        'title': 'Country_List',
        'country_list': country_list
    }
    return render(request, "App_Dashboard/country.html", context=diction)


def country_form(request):
    form = forms.CountryForm()

    if request.method == 'POST':
        form = forms.CountryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('App_Dashboard:country'))
    diction = {
        'title': "Add Country",
        'country_form': form
    }
    return render(request, "App_Dashboard/country_form.html", context=diction)


def edit_country(request, country_id):
    country_info = Country.objects.get(pk=country_id)
    form = forms.CountryForm(instance=country_info)

    if request.method == 'POST':
        form = forms.CountryForm(request.POST, instance=country_info)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('App_Dashboard:country'))
    diction = {
        'edit_form': form
    }
    return render(request, 'App_Dashboard/edit_country.html', context=diction)


def delete_country(request, country_id):
    Country.objects.get(pk=country_id).delete()
    diction = {
        'success': 'Country Deleted Successfully!'
    }
    return HttpResponseRedirect(reverse('App_Dashboard:country'))