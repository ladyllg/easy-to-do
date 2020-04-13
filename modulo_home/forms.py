from django import forms
from .models import *
import datetime
from dateutil.relativedelta import relativedelta

class ConfigForm(forms.Form):
    img = forms.ImageField(required=False)
    newcategory = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type a new category name'}), required=False)
    deletes = forms.CharField(widget=forms.TextInput(), required=False)

class NewTaskForm(forms.Form):
	title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'What do you have to do?'}))
	category = forms.ModelChoiceField(queryset=Category.objects.all(),
												widget=forms.Select(attrs={'class': 'form-control'}))
	due_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'class': 'form-control'}))

	def __init__(self, *args, **kwargs):
		super(NewTaskForm, self).__init__(*args, **kwargs)

		today = datetime.datetime.now()
		date = today + relativedelta(days=1)
		self.fields['due_date'].initial = date.strftime('%Y-%m-%d')
	