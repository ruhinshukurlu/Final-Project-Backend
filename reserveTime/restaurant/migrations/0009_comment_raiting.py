# Generated by Django 3.0.8 on 2020-08-12 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_auto_20200811_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='raiting',
            field=models.IntegerField(blank=True, choices=[(10, '10'), (20, '20'), (30, '30'), (40, '40'), (50, '50')], null=True, verbose_name='Raiting'),
        ),
    ]
