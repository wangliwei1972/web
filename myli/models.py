from django.db import models

# Create your models here.
class Hu1(models.Model):
    xmid = models.FloatField(blank=True, null=True)
    lid = models.FloatField(blank=True, null=True)
    huid = models.CharField(max_length=32, blank=True, null=True)
    xszt = models.CharField(max_length=16, blank=True, null=True)
    dz = models.CharField(max_length=255, blank=True, null=True)
    mp = models.CharField(max_length=50, blank=True, null=True)
    tnmj = models.FloatField(blank=True, null=True)
    ftmj = models.FloatField(blank=True, null=True)
    ytmj = models.FloatField(blank=True, null=True)
    xsmj = models.FloatField(blank=True, null=True)
    jzmj = models.FloatField(blank=True, null=True)
    yt = models.CharField(max_length=16, blank=True, null=True)
    xgrq = models.DateField()
    css = models.FloatField(blank=True, null=True)
    zcs = models.FloatField(blank=True, null=True)
    barq = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hu1'
