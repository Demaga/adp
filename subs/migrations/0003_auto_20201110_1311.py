# Generated by Django 3.1.3 on 2020-11-10 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subs', '0002_sub_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sub',
            name='days',
            field=models.IntegerField(default=1),
        ),
    ]
