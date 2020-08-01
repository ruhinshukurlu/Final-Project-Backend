# Generated by Django 3.0.8 on 2020-08-01 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20200801_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='restaurant.Company', verbose_name='Company'),
        ),
    ]
