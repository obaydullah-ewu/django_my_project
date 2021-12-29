# Generated by Django 2.1.11 on 2021-12-06 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Dashboard', '0008_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='about_us')),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]