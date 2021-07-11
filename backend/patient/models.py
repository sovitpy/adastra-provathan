from django.db import models

# Create your models here.

class Patient(models.Model):
    sex = models.IntegerField()
    chestpain = models.IntegerField()
    angina = models.IntegerField()
    slope = models.IntegerField()
    thalassemia = models.IntegerField()
    heartbeats = models.IntegerField()
    cholestorol = models.FloatField()
    major_vessels= models.IntegerField()
    st_depression = models.FloatField()
    blood_pressure = models.FloatField()


class RiskPercentange(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='risk', related_query_name='risk')
    label = models.CharField(max_length=128)
    value = models.FloatField()

