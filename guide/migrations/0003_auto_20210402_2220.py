# Generated by Django 3.1.7 on 2021-04-02 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0002_nutitionguides'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutitionguides',
            name='description',
            field=models.TextField(blank=True, max_length=254, null=True),
        ),
    ]
