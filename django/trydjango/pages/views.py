from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kwargs):
	# return HttpResponse("<h1>Hello Word</h1>")
	return render(request, "home.html",{})

def contact_view(request,*args,**kwargs):

	# return HttpResponse("<h1>Hello Word</h1>")
	return render(request, "contact.html",{})

def about_view(request,*args,**kwargs):
	my_context = {
		"my_text" : "this is about us",
		"this_is_true" : True,
		"my_number" : 123,
		"my_list" : [1313,4213,312,"Abc"],
		"my_html" : "<h1>hello word</h1>"
	}
	# return HttpResponse("<h1>Hello Word</h1>")
	return render(request, "about.html",my_context)