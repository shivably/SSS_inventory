# Generated by Django 3.0.7 on 2021-09-23 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sales', '0001_initial'),
        ('ledger', '0001_initial'),
        ('retailer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ledger',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ledger_invoice', to='sales.SalesHistory'),
        ),
        migrations.AddField(
            model_name='ledger',
            name='retailer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='retailer_ledger', to='retailer.Retailer'),
        ),
    ]