from django.db import models

# Create your models here.




class Article(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    url = models.URLField()
   

    def __unicode__(self):
        return self.title