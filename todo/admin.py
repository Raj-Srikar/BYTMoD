from django.contrib import admin
import time
from . import views
from . import checker

# Register your models here.
from .models import *

@admin.register(Control)
class ControlAdmin(admin.ModelAdmin):
	list_display = ('control', 'is_opened')
	def has_add_permission(self, request):return False
	def has_delete_permission(self, request, obj=None):return False

	def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
	    extra_context = extra_context or {}
	    extra_context ['show_save_and_continue'] = False
	    return super(ControlAdmin, self).changeform_view(request, object_id, extra_context=extra_context)
	def save_model(self, request, obj, form, change):
		obj.user = request.user
		views.busy = not request.POST.__contains__('field')
		if not views.busy:
			try:
				checker.invl.remove()
			except:
				pass
		else:
			on = time.time()
			on_dur = (views.start + views.dur) - on
			if on_dur > 0:
				try:
					checker.invl.remove()
				except:
					pass
				checker.change_busy(int(on_dur))

		super().save_model(request, obj, form, change)
