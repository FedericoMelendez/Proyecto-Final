# Generated by Django 4.0.6 on 2022-09-04 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_address_user_profile_adress_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_image/'),
        ),
    ]
