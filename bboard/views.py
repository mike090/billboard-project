from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import BillBoard

# Create your views here.

def index(request):
	template = loader.get_template('bboard/index.html')
	bbs = BillBoard.objects.all()
	context = {'bbs': bbs}
	return HttpResponse(template.render(context, request))