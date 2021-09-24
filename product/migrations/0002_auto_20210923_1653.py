# Generated by Django 3.0.7 on 2021-09-23 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sales', '0001_initial'),
        ('com', '0001_initial'),
        ('product', '0001_initial'),
        ('retailer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockout',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='out_invoice', to='sales.SalesHistory'),
        ),
        migrations.AddField(
            model_name='stockout',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stockout_product', to='product.Product'),
        ),
        migrations.AddField(
            model_name='stockout',
            name='purchased_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='out_purchased', to='product.PurchasedProduct'),
        ),
        migrations.AddField(
            model_name='stockin',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stockin_product', to='product.Product'),
        ),
        migrations.AddField(
            model_name='purchasedproduct',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchased_invoice', to='sales.SalesHistory'),
        ),
        migrations.AddField(
            model_name='purchasedproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchased_product', to='product.Product'),
        ),
        migrations.AddField(
            model_name='productdetail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_detail', to='product.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='retailer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='retailer_product', to='retailer.Retailer'),
        ),
        migrations.AddField(
            model_name='extraitems',
            name='retailer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='retailer_extra_items', to='retailer.Retailer'),
        ),
        migrations.AddField(
            model_name='claimedproduct',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_claimed_items', to='com.Customer'),
        ),
        migrations.AddField(
            model_name='claimedproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claimed_product', to='product.Product'),
        ),
    ]