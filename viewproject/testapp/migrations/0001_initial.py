# Generated by Django 3.1.5 on 2022-02-03 14:27

from django.db import migrations, models
import testapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubbuModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, validators=[testapp.models.clean])),
                ('desc', models.TextField()),
            ],
        ),
    ]
