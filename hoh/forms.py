from django import forms
from django.forms import ModelForm,PasswordInput
from models import *
		
class contestant_infoForm(forms.ModelForm):
	class Meta:
		model = contestant_info
		fields = '__all__'