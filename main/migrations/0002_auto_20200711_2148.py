# Generated by Django 2.1.5 on 2020-07-11 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='date published',
            field=models.DateTimeField(),
        ),
    ]