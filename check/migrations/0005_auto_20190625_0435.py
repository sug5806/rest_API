# Generated by Django 2.2.2 on 2019-06-25 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0004_remove_test_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='test_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
