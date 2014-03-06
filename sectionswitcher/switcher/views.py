from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import render
from switcher.models import *
from django.core.urlresolvers import reverse

def home(request):
	return render_to_response("switcher/home.html")

def thanks(request):
	if request.method == 'GET':
		return HttpResponse(request.GET['departments'])

		