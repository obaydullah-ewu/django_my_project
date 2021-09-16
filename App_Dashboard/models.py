from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50)
    isd_code = models.CharField(max_length=20)
    currency = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    status_ = (
        (1, "Active"),
        (2, "Deactivate")
    )
    status = models.IntegerField(choices=status_)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


