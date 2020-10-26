from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.
from django.views.generic import (
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView
	)

from .models import user
from .forms import CreateForm


def index(request): 
    return render(request, 'index.html')

class Create_View(CreateView):
	template_name = 'pages/page_create.html'
	form_class = CreateForm
	queryset = user.objects.all()  #<blog>/<modelname>_list.html

	def form_valid(self,form):
		print(form.cleaned_data)
		return super().form_valid(form)

class List_View(ListView):
	template_name = 'pages/page_list.html'
	queryset = user.objects.all()  #<blog>/<modelname>_list.html

class Detail_View(DetailView):
	template_name = 'pages/page_detail.html'
	queryset = user.objects.all()  #<blog>/<modelname>_list.html

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(user,id=id_)

class Update_View(UpdateView):
	template_name = 'pages/page_create.html'
	form_class = CreateForm
	queryset = user.objects.all()

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(user,id=id_)

	def form_valid(self,form):
		print(form.cleaned_data)
		return super().form_valid(form)

class Delete_View(DeleteView):
	template_name = 'pages/page_delete.html'
	# queryset = user.objects.all()  #<blog>/<modelname>_list.html

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(user,id=id_)

	def get_success_url(self):
		return reverse('lpzx:lpzx-list')