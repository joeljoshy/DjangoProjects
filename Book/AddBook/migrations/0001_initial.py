# Generated by Django 3.2.5 on 2021-07-20 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=70, unique=True)),
                ('author', models.CharField(max_length=15)),
                ('category', models.CharField(max_length=20)),
                ('price', models.FloatField(default=50)),
                ('copies', models.IntegerField()),
            ],
        ),
    ]