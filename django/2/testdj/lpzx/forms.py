from django import forms

from .models import user

class CreateForm(forms.ModelForm):

	class Meta:
		model = user
		fields = [
			'comname',
			'groupname',
			'usercode',
			'username',
			'post',
			'postcode'
		]
