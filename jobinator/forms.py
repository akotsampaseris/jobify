from django import forms

class JobinatorForm(forms.Form):
    position = forms.CharField(label='Position', max_length=100)
    location = forms.CharField(label='Location', max_length=100)
