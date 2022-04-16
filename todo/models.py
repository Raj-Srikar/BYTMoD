from django.db import models

# Create your models here.

class Control(models.Model):
	field = models.CharField(max_length=255, null=False)
	def __str__(self):return self.field