from django.db import models


# Create your models here.
class abc(models.Model):
      name=models.CharField(max_length=20)
      sallary=models.CharField(max_length=20)
      active=models.BooleanField()

      def __str__(self):
            return self.name