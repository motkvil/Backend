# Generated by Django 2.2.14 on 2021-12-23 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category2', '0004_auto_20211222_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='comment',
            field=models.ManyToManyField(blank=True, related_name='article_comment', to='category2.Comment'),
        ),
    ]
