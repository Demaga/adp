# Generated by Django 3.1.3 on 2020-11-10 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subs', '0004_auto_20201110_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='sub',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
