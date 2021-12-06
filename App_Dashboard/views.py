from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from App_Dashboard import forms
from App_Dashboard.forms import PostForm
from App_Dashboard.models import Country, DesignerInfo, Post, AboutUs, ContactUs, React
from App_Login.models import UserProfile


# @login_required
def home(request):
    country_list = Country.objects.all()
    customers_count = UserProfile.objects.filter(type=1)
    designers_count = UserProfile.objects.filter(type=2)
    designers = UserProfile.objects.filter(type=2)
    aboutus = AboutUs.objects.all()
    diction = {
        'title': 'Dashboard',
        'country_list': country_list,
        'customers_count': customers_count,
        'designers_count': designers_count,
        'designers': designers,
        'aboutus': aboutus
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
def designer_info(request):
    designers = DesignerInfo.objects.all()
    print(designers)
    diction = {
        'title': 'Designer Info',
        'designers': designers,
    }
    return render(request, "App_Dashboard/designers_list.html", context=diction)


@login_required
def add_designer(request):
    form = forms.DesignerInfoForm()

    if request.method == 'POST':
        form = forms.DesignerInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Designer Info Added Successfully')
            return HttpResponseRedirect(reverse('App_Dashboard:designer_info'))
    diction = {
        'title': "Add Designer Info",
        'designer_info_form': form
    }
    return render(request, "App_Dashboard/designers_form.html", context=diction)


@login_required
def view_designer(request, designer_id):
    designer = UserProfile.objects.get(pk=designer_id)
    posts = Post.objects.filter(author_id=designer.user.id)

    diction = {
        'title': 'Designer Details',
        'designer': designer,
        'posts': posts,
    }
    return render(request, 'App_Dashboard/view_designers.html', context=diction)


@login_required
def edit_designer(request, designer_id):
    designer_info = DesignerInfo.objects.get(pk=designer_id)
    form = forms.DesignerInfoForm(instance=designer_info)

    if request.method == 'POST':
        form = forms.DesignerInfoForm(request.POST, request.FILES, instance=designer_info)

        if form.is_valid():
            form.save(commit=True)
            messages.info(request, 'Designer Updated Successfully')
            return HttpResponseRedirect(reverse('App_Dashboard:designer_info'))
    diction = {
        'edit_form': form
    }
    return render(request, 'App_Dashboard/edit_designers.html', context=diction)


@login_required
def delete_designer(request, designer_id):
    DesignerInfo.objects.get(pk=designer_id).delete()
    messages.success(request, 'Designer Deleted Successfully')
    return HttpResponseRedirect(reverse('App_Dashboard:designer_info'))

@login_required
def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Designer Post Added Successfully')
            return HttpResponseRedirect(reverse('App_Login:profile'))
    diction = {
        'title': "Profile Info",
    }
    return render(request, "App_Login/user.html", context=diction)


def view_posts(request):
    posts = Post.objects.all()
    diction = {
        'title': 'Blog Post',
        'posts': posts,
    }
    return render(request, 'App_Dashboard/view_posts.html', context=diction)


def contactUs(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        message = request.POST['message']
        data_dict = {
            'name': name,
            'email': email,
            'contact': contact,
            'message': message,
        }
        ContactUs.objects.create(**data_dict)
        messages.success(request, 'Message has been sent successfully ')
        return HttpResponseRedirect(reverse('App_Dashboard:home'))


def aboutUs(request):
    aboutus = AboutUs.objects.all()


def like_post(request, post_id):
    react = React.objects.filter(post=post_id, user=request.user)

    if react.count() < 1:
        data_dict = {
            'user': request.user,
            'post': post_id,
        }
        React.objects.create(**data_dict)
        messages.success(request, 'You like the post successfully')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def unlike_post(request, post_id):
    react = React.objects.filter(post=post_id, user=request.user).delete()
    messages.success(request, 'You like the post successfully')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))