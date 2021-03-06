# Generated by Django 3.0.8 on 2020-08-30 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0021_auto_20200828_0823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='times',
        ),
        migrations.AddField(
            model_name='tabledate',
            name='times',
            field=models.ManyToManyField(to='restaurant.Time', verbose_name='Time'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notified_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Notification date'),
        ),
    ]
