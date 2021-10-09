from django.db import models

class Posts (models.Model):

    name = models.CharField(max_length=50)
    content = models.TextField()
    date = models.TimeField()

    def __str__(self): 
        return self.name
