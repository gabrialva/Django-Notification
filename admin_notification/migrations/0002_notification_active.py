# Generated by Django 4.0.6 on 2022-08-02 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_notification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]