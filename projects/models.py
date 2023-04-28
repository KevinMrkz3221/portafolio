from django.db import models

# Create your models here.


class Projects(models.Model):
    my_choises = (
        ('WEB', ' Web'),
        ('DESKTOP', 'Desktop'),
        ('ANALYSIS', 'Analysis'),
    )
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=my_choises, default='WEB')
    client = models.CharField(max_length=50)
    project_date = models.DateField()
    project_url = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to='static/images')

class Pictures(models.Model):
    image = models.ImageField(upload_to='static/images')
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='Pictures')