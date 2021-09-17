from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50)
    isd_code = models.CharField(max_length=20)
    currency = models.CharField(max_length=20)
    phone_digit = models.CharField(max_length=20)
    status_ = (
        (1, "Active"),
        (2, "Deactivate")
    )
    status = models.IntegerField(choices=status_)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TaxiCompany(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=None, related_name='country_info')
    logo = models.ImageField(upload_to='profile_pics', blank=True)
    company_details = models.CharField(max_length=264)
    url = models.CharField(max_length=264)
    address = models.CharField(max_length=264)
    status_ = (
        (1, "Active"),
        (2, "Deactivate")
    )
    status = models.IntegerField(choices=status_)

    def __str__(self):
        return self.country.name


