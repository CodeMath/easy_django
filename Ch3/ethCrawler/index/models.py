from django.db import models

# Create your models here.
class History(models.Model):
    name = models.CharField(max_length=255, verbose_name="암호화폐")
    date = models.DateTimeField(auto_now_add=True)
    asks = models.CharField(max_length=200, verbose_name="asks")
    bids = models.CharField(max_length=200, verbose_name="bids")

    asks_vol = models.CharField(max_length=200, verbose_name="asks vol")
    bids_vol = models.CharField(max_length=200, verbose_name="bids vol")

    def __str__(self):
        return self.name