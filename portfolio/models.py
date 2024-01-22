from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

class Project(models.Model):
    title = CharField(max_lenght=100)
    description = CharField(max_lenght=250)
    image = ImageField(upload_to='portfolio/imagens')
    url = URLField(blank=True)