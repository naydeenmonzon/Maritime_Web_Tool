# Generated by Django 3.2.8 on 2021-10-15 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0004_templateresponse'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='tools',
            index=models.Index(fields=['urlNAME'], name='urlNAME_idx'),
        ),
    ]
