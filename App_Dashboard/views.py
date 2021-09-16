from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from App_Dashboard import forms
from App_Dashboard.models import Country


@login_required
def home(request):
    country_list = Country.objects.all()
    diction = {
        'title': 'Dashboard',
        'country_list': country_list
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
    diction = {
        'title': "Add Country",
        'country_form': form
    }
    return render(request, "App_Dashboard/country_form.html", context=diction)
