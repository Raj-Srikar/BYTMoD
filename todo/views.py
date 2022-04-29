from django.shortcuts import render
from django.http import HttpResponse

from .forms import NameForm
from . import checker

import webbrowser
import pafy
from random import randint


busy = False
dur=None
embedded = ''

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
		busy=True
		try:
			vid = pafy.new(link)
			dur = vid.length
			rcode = ''.join([chr(randint(65,91))+chr(randint(97,123))+chr(randint(48,58)) for x in range(3)])
			webbrowser.open('http://127.0.0.1:8000/video?v='+link+'&r='+rcode)
			checker.change_busy()
			return render(request, 'response.html', {'response':'<h1>Thank You!</h1>'})
		except:
			busy=False
			return render(request, 'response.html', {'response':'<h1>Bad URL!</h1><p>Provide a proper YouTube link</p>'})
	else:
		return render(request, 'response.html', {'response':'<h2>The player is busy. Please try again later!</h2>'})
		

def video(request):
	r = request.GET
	link = dict(r)['v'][0]
	embedded = embed(link)
	return render(request, 'video.html', {'link': embedded})




def embed(link):
    link = link.replace('?t', '?start')
    link = link.replace('&t','?start')
    link = link.replace('m.','')
    embeded = link.replace('watch?v=','embed/')
    if link == embeded: embeded = link.replace('youtu.be', 'youtube.com/embed')
    embeded = embeded + '&' if '?start' in embeded else embeded+'?'
    return embeded