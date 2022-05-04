from django.db import models
from . import views

# Create your models here.

class Control(models.Model):
	field = models.BooleanField('Make the player available to accept new song requests.',default=False)
	def __str__(self):return "Open for New Song Requests"
	def control(self):
		return 'Open for new song requests'
	def is_opened(self):
		return bool(int(self.field))
	is_opened.boolean = True

def set_val():
	Control.objects.filter(id=1).update(field = not views.busy)

set_val()
