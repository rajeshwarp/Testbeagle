from django.db import models


# Create your models here.

class Test(models.Model):
    testName = models.CharField(max_length= 500)
    testDescription = models.CharField(max_length= 500)
    stepkey = models.ForeignKey('Step',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f'{self.testName})'

class Step(models.Model):
    stepName = models.CharField(max_length= 500)
    stepDescription = models.CharField(max_length= 500)
    params  = models.TextField()
    
    def __str__(self):
        return f'{self.stepName}'
