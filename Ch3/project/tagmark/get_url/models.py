from django.db import models

class Tag(models.Model):
    text = models.CharField(max_length=250,verbose_name="태그")

    def __str__(self):
        return self.text

class Bookmark(models.Model):

    url = models.URLField(max_length=250, verbose_name="웹사이트")
    tag = models.ManyToManyField( Tag, related_name="Tag")
    create = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url