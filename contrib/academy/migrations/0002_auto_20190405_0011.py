# Generated by Django 2.1.7 on 2019-04-04 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='major',
            name='research',
        ),
        migrations.AddField(
            model_name='major',
            name='maj_type',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.DeleteModel(
            name='Research',
        ),
    ]
