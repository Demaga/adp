# Generated by Django 3.1.3 on 2020-11-10 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subs', '0003_auto_20201110_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
