from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.views.generic import (
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DetailView
	)

from .models import user

class List_View(ListView):
	template_name = 'pages/page_list.html'
	queryset = user.objects.all()  #<blog>/<modelname>_list.html

class Detail_View(DetailView):
	template_name = 'pages/page_detail.html'
	queryset = user.objects.all()  #<blog>/<modelname>_list.html

	def get_object(self):
		id_ = self.kwargs.get("id")

		return get_object_or_404(user,id=id_)