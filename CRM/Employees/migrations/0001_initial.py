# Generated by Django 3.2.5 on 2021-07-24 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=70)),
                ('desig', models.CharField(max_length=30)),
                ('salary', models.FloatField(default=50)),
                ('exp', models.IntegerField()),
                ('email', models.EmailField(max_length=250, unique=True)),
            ],
        ),
    ]
