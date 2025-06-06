# Generated by Django 5.1.7 on 2025-03-21 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_sitetext_test1_author_sitetext_test1_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitetext',
            name='test1_text',
            field=models.CharField(default='The guys from Aria helped with getting my business off the ground and turning into a profitable company.', max_length=300),
        ),
        migrations.AlterField(
            model_name='sitetext',
            name='test2_text',
            field=models.CharField(default='I purchased the Growth Accelerator service pack a few years ago and I renewed the contract each year.', max_length=300),
        ),
        migrations.AlterField(
            model_name='sitetext',
            name='test3_text',
            field=models.CharField(default="Aria's CEO personally attends client meetings and gives his feedback on business growth strategies.", max_length=300),
        ),
        migrations.AlterField(
            model_name='sitetext',
            name='test4_text',
            field=models.CharField(default='At the beginning I thought the prices are a little high for what they offer but they over deliver each and every time.', max_length=300),
        ),
        migrations.AlterField(
            model_name='sitetext',
            name='test5_text',
            field=models.CharField(default='I recommend Aria to every business owner or growth leader that wants to take his company to the next level.', max_length=300),
        ),
        migrations.AlterField(
            model_name='sitetext',
            name='test6_text',
            field=models.CharField(default="My goals for using Aria's services seemed high when I first set them but they've met them with no problems.", max_length=300),
        ),
    ]
