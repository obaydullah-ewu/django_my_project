# Generated by Django 2.1.11 on 2021-12-03 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0003_auto_20210917_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='type',
            field=models.CharField(blank=True, max_length=264),
        ),
    ]
