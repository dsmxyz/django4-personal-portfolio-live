from django.db import models

# Project model
class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to='portfolio/images/')
    url=models.URLField(blank=True)
    # Function to return database query(title) as a string
    def __str__(self):
        return self.title

