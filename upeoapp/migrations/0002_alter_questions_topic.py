# Generated by Django 4.1.1 on 2022-10-27 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upeoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='topic',
            field=models.TextField(null=True),
        ),
    ]
