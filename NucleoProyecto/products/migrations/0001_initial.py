# Generated by Django 4.1 on 2022-08-24 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notebooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=100)),
                ('processor', models.CharField(max_length=100)),
                ('ram', models.CharField(max_length=100)),
                ('display', models.CharField(max_length=50)),
                ('capacity', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('is_active', models.BooleanField(default=True)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]