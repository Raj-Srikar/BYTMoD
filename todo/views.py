from django.shortcuts import render
from django.http import HttpResponse

from .forms import NameForm
from . import checker

import webbrowser
import pafy


busy = False
dur=None

# Create your views here.
def index(request):
	return render(request, 'todo/index.html')

		
def get_link(request):
    busy=False
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print(form.cleaned_data['yt_link'])
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    
    return render(request, 'input.html', {'form': form})
    
def yt_link(request):
	global busy
	global dur
	if not busy:
		r=request.POST
		link = dict(r)['yt_link'][0]
		try:
			vid = pafy.new(link)
			dur = vid.length
			webbrowser.open(link)
			busy=True
			checker.change_busy()
			return HttpResponse('<h1>Thank You!</h1>')
		except:
			return HttpResponse('<h1>Bad URL!</h1><p>Provide a proper YouTube link</p>')
	else:
		return HttpResponse('<h3>The player is busy. Please try again later!</h3>')
	#return render(request, 'video.html', {'link': inp})
