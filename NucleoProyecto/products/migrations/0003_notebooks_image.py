# Generated by Django 4.1 on 2022-09-01 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_monitores_perifericos_alter_notebooks_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebooks',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='notebooks/'),
        ),
    ]
