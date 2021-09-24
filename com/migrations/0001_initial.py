# Generated by Django 3.0.7 on 2021-09-23 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('retailer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production', models.BooleanField(default=False)),
                ('demo', models.BooleanField(default=False)),
                ('local', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('shop', 'Shop'), ('company', 'Company'), ('individual', 'Individual')], default='shop', max_length=100)),
                ('address', models.TextField(blank=True, max_length=512, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=13, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=13, null=True)),
                ('picture', models.ImageField(blank=True, max_length=1024, upload_to='images/profile/picture/')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('retailer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='retailer_feedback', to='retailer.Retailer')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=200)),
                ('customer_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('customer_type', models.CharField(blank=True, default='customer', max_length=200, null=True)),
                ('address', models.TextField(blank=True, max_length=500, null=True)),
                ('shop', models.CharField(blank=True, max_length=200, null=True)),
                ('retailer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='retailer_customer', to='retailer.Retailer')),
            ],
        ),
    ]