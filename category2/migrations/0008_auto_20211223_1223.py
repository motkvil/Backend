# Generated by Django 2.2.14 on 2021-12-23 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category2', '0007_auto_20211222_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='alias',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
