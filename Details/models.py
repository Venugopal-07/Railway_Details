from django.db import models

# Create your models here.
class Train_Details(models.Model):
    Train_No=models.IntegerField()
    Train_Name=models.CharField(max_length=50)
    Source=models.CharField(max_length=30)
    Destination=models.CharField(max_length=30)
    def __str__(self):
        return self.Train_Name+ "  "+str('self.Train_No')
     