from django.db import models


# Create your models here.


class Doctor(models.Model):
   d_id = models.CharField(max_length=100,primary_key=True)
   d_name = models.CharField(max_length=200)
   qualifications = models.CharField(max_length=100)
   experience = models.IntegerField()
   Rating = models.FloatField()
   No_of_awards = models.IntegerField()

class patient(models.Model):
   p_id = models.CharField(max_length=10,primary_key=True)
   p_name = models.CharField(max_length=25)
   disease_name = models.CharField(max_length=15)
   age = models.IntegerField()
   sex = models.CharField(max_length=10)

class clinic(models.Model):
   c_id = models.CharField(max_length=10,primary_key=True)
   c_name = models.CharField(max_length=30)
   address = models.CharField(max_length=35)
   doctor_id = models.ForeignKey(Doctor,on_delete=models.CASCADE)

class medication(models.Model):
   pre_id = models.CharField(max_length=10,primary_key=True)
   medicines = models.CharField(max_length=20)
   patient_id = models.ForeignKey(patient,on_delete=models.CASCADE)

