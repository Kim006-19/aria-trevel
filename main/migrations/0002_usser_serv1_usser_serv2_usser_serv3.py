# Generated by Django 5.1.7 on 2025-03-18 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usser',
            name='serv1',
            field=models.ImageField(blank=True, null=True, upload_to='serv1/'),
        ),
        migrations.AddField(
            model_name='usser',
            name='serv2',
            field=models.ImageField(blank=True, null=True, upload_to='serv2/'),
        ),
        migrations.AddField(
            model_name='usser',
            name='serv3',
            field=models.ImageField(blank=True, null=True, upload_to='serv3/'),
        ),
    ]
