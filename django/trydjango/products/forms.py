from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	title      = forms.CharField(label='',
			widget=forms.Textarea(attrs={"placeholder":"your product title"}))
	# email 	   = forms.EmailField()
	description= forms.CharField(
				 required=False,
				 widget=forms.Textarea(
				 	attrs={
				 		"placeholder":"your title",
				 		"class":"new-class-name two",
				 		"id":"my-id-for-textarea",
				 		"row":20,
				 		"cols":120
				 	})
				 )
	price      = forms.DecimalField(initial=199.99)

	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price'
		]

	# def clean_title(self,*args,**kwargs):
	# 	print("im here")
	# 	title = self.cleaned_data.get("title")
	# 	# title = self.cleaned_date.get("title")
	# 	print("im here again")
	# 	if not "CFE" in title:
	# 		raise forms.ValidationError("this is not a bbb valid title")
	# 	if not "news" in title:
	# 		raise forms.ValidationError("this is not a valid title")
	# 	return title

	# def clean_email(self,*args,**kwargs):
	# 	email = self.cleaned_data.get('email')
	# 	if not email.endswith("edu"):
	# 		raise forms.ValidationError("this is not a valid email")
	# 	return email


class RawProductForm(forms.Form):
	title      = forms.CharField(label='dsf',
		widget=forms.Textarea(attrs={"placeholder":"your title"}))
	description= forms.CharField(
				 required=False,
				 widget=forms.Textarea(
				 	attrs={
				 		"placeholder":"your title",
				 		"class":"new-class-name two",
				 		"id":"my-id-for-textarea",
				 		"row":20,
				 		"cols":120
				 	})
				 )
	price      = forms.DecimalField(initial=199.99)