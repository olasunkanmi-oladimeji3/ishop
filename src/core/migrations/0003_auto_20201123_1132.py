# Generated by Django 2.2 on 2020-11-23 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201122_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='billingaddress',
        ),
        migrations.AddField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_address', to='core.BillingAddress'),
        ),
    ]
