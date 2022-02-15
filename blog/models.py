from django.db import models

# Blog model
class Blog(models.Model):
    title=models.CharField(max_length=250)
    description=models.TextField()
    date=models.DateField()
    # Function to return database query(title) as a string
    def __str__(self):
        return self.title