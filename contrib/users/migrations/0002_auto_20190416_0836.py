# Generated by Django 2.1.7 on 2019-04-16 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stu_gain_cert',
            field=models.BooleanField(default=False, help_text='毕业证', null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='stu_gain_diploma',
            field=models.BooleanField(default=False, help_text='学位证', null=True),
        ),
    ]
