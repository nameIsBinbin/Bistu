# Generated by Django 2.1.7 on 2019-04-05 16:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academy',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='唯一标识ID', primary_key=True, serialize=False, unique=True)),
                ('aca_name', models.CharField(help_text='学院名称', max_length=128, null=True)),
                ('aca_code', models.IntegerField(help_text='学院代码', null=True)),
            ],
            options={
                'verbose_name': '学院',
                'verbose_name_plural': '学院',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='唯一标识ID', primary_key=True, serialize=False, unique=True)),
                ('maj_name', models.CharField(help_text='学科专业名称', max_length=128, null=True)),
                ('maj_code', models.IntegerField(help_text='学科专业编号', null=True)),
                ('maj_type', models.CharField(max_length=128, null=True)),
            ],
            options={
                'verbose_name': '学科专业',
                'verbose_name_plural': '学科专业',
            },
        ),
        migrations.AddField(
            model_name='academy',
            name='majors',
            field=models.ManyToManyField(related_name='majors', to='academy.Major'),
        ),
    ]