# Generated by Django 4.2.5 on 2023-10-16 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-04-28'),
            preserve_default=False,
        ),
    ]
