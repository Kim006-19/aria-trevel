# Generated by Django 5.1.7 on 2025-03-16 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/')),
                ('img', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('img1', models.ImageField(blank=True, null=True, upload_to='img1/')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='img2/')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='img3/')),
                ('img4', models.ImageField(blank=True, null=True, upload_to='img4/')),
                ('img5', models.ImageField(blank=True, null=True, upload_to='img5/')),
                ('img6', models.ImageField(blank=True, null=True, upload_to='img6/')),
                ('img7', models.ImageField(blank=True, null=True, upload_to='img7/')),
                ('img8', models.ImageField(blank=True, null=True, upload_to='img8/')),
            ],
        ),
    ]
