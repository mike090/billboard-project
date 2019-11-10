from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import BillBoard, Rubric
from .forms import BillBoardForm

# Create your views here.

def index(request):
	template = loader.get_template('bboard/index.html')
	bbs = BillBoard.objects.all()
	rubrics = Rubric.objects.all()
	context = {'bbs': bbs, 'rubrics': rubrics}
	return HttpResponse(template.render(context, request))

def by_rubric(request, rubric_id):
	current_rubric = Rubric.objects.get(pk=rubric_id)
	rubrics = Rubric.objects.all()
	bbs = BillBoard.objects.filter(rubric=rubric_id)
	context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
	return render(request, 'bboard/by_rubric.html', context)

class BillBoardCreateView(CreateView):
	template_name = 'bboard/create.html'
	form_class = BillBoardForm
	success_url = reverse_lazy('index')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['rubrics'] = Rubric.objects.all()
		return context
		