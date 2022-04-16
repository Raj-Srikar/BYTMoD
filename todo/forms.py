from django import forms

class NameForm(forms.Form):
    yt_link = forms.CharField(label='YouTube Link', max_length=100)
    