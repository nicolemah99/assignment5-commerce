# Generated by Django 4.1.2 on 2022-10-23 21:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_alter_listing_dateposted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='dateBidEnd',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='listing',
            name='datePosted',
            field=models.DateField(default=datetime.date.today),
        ),
    ]