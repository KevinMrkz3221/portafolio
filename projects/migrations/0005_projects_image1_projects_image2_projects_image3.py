# Generated by Django 4.2 on 2023-04-28 22:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_projects_description_alter_projects_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='image1',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='static/images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='image2',
            field=models.ImageField(default='', upload_to='static/images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='image3',
            field=models.ImageField(default='', upload_to='static/images'),
            preserve_default=False,
        ),
    ]