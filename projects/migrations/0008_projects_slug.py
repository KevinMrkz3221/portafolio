# Generated by Django 4.2 on 2023-04-28 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_remove_projects_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='slug',
            field=models.SlugField(auto_created=True, default='', unique=True),
            preserve_default=False,
        ),
    ]
