# Generated by Django 4.2.10 on 2024-07-24 19:16

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Intern Ease', help_text='Application name', max_length=100)),
                ('short_name', models.CharField(default='EE', help_text='Your application short name', max_length=10)),
                ('tagline', models.CharField(default='Empowering Futures through Collaboration', help_text='Your application business line', max_length=100)),
                ('description', models.TextField(default='Connect companies offering enriching internships with aspiring students seeking valuable experiences', help_text='Application description')),
                ('favicon', models.ImageField(blank=True, help_text='Application favicon', null=True, upload_to='core/application/images')),
                ('logo', models.ImageField(blank=True, help_text='Application real colors logo', null=True, upload_to='core/application/images')),
                ('logo_dark', models.ImageField(blank=True, help_text='For dark theme only', null=True, upload_to='core/application/images')),
                ('logo_light', models.ImageField(blank=True, help_text='For light theme only', null=True, upload_to='core/application/images')),
                ('contact_email1', models.EmailField(default='support@internease.com', help_text='Application contact email 1', max_length=100)),
                ('contact_email2', models.EmailField(default='support@internease.com', help_text='Application contact email 2', max_length=100)),
                ('contact_phone1', phonenumber_field.modelfields.PhoneNumberField(default='+10000000000', help_text='Application contact phone 1', max_length=128, region=None)),
                ('contact_phone2', phonenumber_field.modelfields.PhoneNumberField(default='+10000000000', help_text='Application contact phone 2', max_length=128, region=None)),
                ('address', models.CharField(default='XYZ, City, Country', help_text='Office address', max_length=255)),
                ('latitude', models.DecimalField(decimal_places=6, default=23.7, help_text='Latitude', max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=6, default=90.3, help_text='Longitude', max_digits=10)),
                ('terms_url', models.URLField(default='https://internease.com/terms-of-use/', help_text='Terms and Conditions page link', max_length=255)),
                ('version', models.CharField(default='1.0.0', help_text='Current version', max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Application',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Contact name', max_length=100)),
                ('email', models.EmailField(help_text='Contact email', max_length=100)),
                ('message', models.TextField(help_text='Contact message')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Contact',
                'ordering': ['name'],
            },
        ),
    ]
