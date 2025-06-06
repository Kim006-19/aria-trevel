# Generated by Django 5.1.7 on 2025-03-27 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_contactrequest_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactRequest2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('message', models.CharField(blank=True, max_length=255, null=True)),
                ('agreed_to_terms', models.BooleanField(default=False)),
            ],
        ),
    ]
