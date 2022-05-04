from . import views
from . import models
from apscheduler.schedulers.background import BackgroundScheduler as bs
import time

sch = bs()
invl=None

def job():
	global invl, on
	views.busy=False
	models.set_val()
	on = 0
	try:
		invl.remove()
	except:
		pass

def change_busy(dur):
	global invl
	print(dur)
	sch = bs()
	invl = sch.add_job(job, 'interval', seconds=dur+5, id='my_delay')
	sch.start()
