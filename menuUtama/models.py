from django.db import models
from datetime import datetime, timezone

# Create your models here.
class PostUser(models.Model):
    nama = models.CharField(max_length=50, blank=True, null=True)
    satker = models.CharField(max_length=25, blank=True, null=True)
    
    def __str__(self):
        return self.nama

class PostSatker(models.Model):
    satker = models.CharField(max_length=25, blank=True, null=True)
    
    def __str__(self):
        return self.satker

class PostRuangan(models.Model):
    ruangan = models.CharField(max_length=25, blank=False, null=True)
    kapasitas = models.CharField(max_length=25)

    def __str__(self):
        return self.ruangan
    
class PostData(models.Model):
    nama = models.ForeignKey(PostUser, on_delete=models.CASCADE)
    satker = models.ForeignKey(PostSatker, on_delete=models.CASCADE)
    ruangan = models.ForeignKey(PostRuangan, on_delete=models.CASCADE)
    waktu = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False, null=False, default=timezone.utc)
    keterangan = models.TextField(blank=False, null=False)

    def __str__(self):
        return "{}".format (self.nama)

    