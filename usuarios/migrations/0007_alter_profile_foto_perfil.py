# Generated by Django 4.1 on 2022-09-08 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='foto_perfil',
            field=models.FileField(blank=True, upload_to='static'),
        ),
    ]
