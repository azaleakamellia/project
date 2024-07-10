from django.contrib.gis.db import models

# Create your models here.

class ns(models.Model):
    type = models.CharField(max_length=254, null=True)
    client_gov = models.CharField(max_length=254, null=True)
    handle = models.CharField(max_length=16, null=True)
    layer = models.CharField(max_length=254, null=True)
    lyrhandle = models.CharField(max_length=16, null=True)
    elevation = models.FloatField(null=True)
    refname = models.CharField(max_length=254, null=True)
    docname = models.CharField(max_length=254, null=True)
    docpath = models.CharField(max_length=254, null=True)
    doctype = models.CharField(max_length=32, null=True)
    docver = models.CharField(max_length=16, null=True)
    docupdate = models.DateField(null=True)
    globalwidt = models.FloatField(null=True)
    shape_leng = models.FloatField(null=True)
    geom = models.MultiLineStringField()

    def __str__(self):
        return self.layer


class wp(models.Model):
    type = models.CharField(max_length=254, null=True)
    client_gov = models.CharField(max_length=254, null=True)
    handle = models.CharField(max_length=16, null=True)
    layer = models.CharField(max_length=254, null=True)
    lyrhandle = models.CharField(max_length=16, null=True)
    elevation = models.FloatField(null=True)
    refname = models.CharField(max_length=254, null=True)
    docname = models.CharField(max_length=254, null=True)
    doctype = models.CharField(max_length=32, null=True)
    docver = models.CharField(max_length=16, null=True)
    docupdate = models.DateField(null=True)
    globalwidt = models.FloatField(null=True)
    shape_leng = models.FloatField(null=True)
    geom = models.MultiLineStringField()

    def __str__(self):
        return self.layer


class pl(models.Model):
    type = models.CharField(max_length=254, null=True)
    client_gov = models.CharField(max_length=254, null=True)
    handle = models.CharField(max_length=16, null=True)
    layer = models.CharField(max_length=254, null=True)
    lyrhandle = models.CharField(max_length=16, null=True)
    elevation = models.FloatField(null=True)
    refname = models.CharField(max_length=254, null=True)
    docname = models.CharField(max_length=254, null=True)
    doctype = models.CharField(max_length=32, null=True)
    docver = models.CharField(max_length=16, null=True)
    docupdate = models.DateField(null=True)
    globalwidt = models.FloatField(null=True)
    shape_leng = models.FloatField(null=True)
    geom = models.MultiLineStringField()

    def __str__(self):
        return self.layer


class rd(models.Model):
    type = models.CharField(max_length=254, null=True)
    client_gov = models.CharField(max_length=254, null=True)
    handle = models.CharField(max_length=16, null=True)
    layer = models.CharField(max_length=254, null=True)
    lyrhandle = models.CharField(max_length=16, null=True)
    elevation = models.FloatField(null=True)
    refname = models.CharField(max_length=254, null=True)
    docname = models.CharField(max_length=254, null=True)
    doctype = models.CharField(max_length=32, null=True)
    docver = models.CharField(max_length=16, null=True)
    docupdate = models.DateField(null=True)
    globalwidt = models.FloatField(null=True)
    shape_leng = models.FloatField(null=True)
    geom = models.MultiLineStringField(srid=4326)

    def __self__(self):
        return self.layer
