# Generated by Django 4.2 on 2023-04-28 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_projects_name_pictures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='image',
            field=models.ImageField(upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='main_image',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
