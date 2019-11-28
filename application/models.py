from django.db import models

# Create your models here.

class careers(models.Model):
    career_name = models.CharField(max_length =200)


class allcourses(models.Model):
    course_id = models.IntegerField()
    pro_code = models.IntegerField()
    university = models.CharField(max_length=200)
    course_name = models.CharField(max_length=200)
    cp = models.FloatField()
    cutoffpoints_2014= models.FloatField()
    cutoffpoints_2015_cp= models.FloatField()
    cutoffpoints_2016_cp= models.FloatField()
    cutoffpoints_2017_cp= models.FloatField()
    cutoffpoints_2018_cp= models.FloatField()
    course_id = models.ForeignKey(careers)
