from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import render
from switcher.models import *
from django.core.urlresolvers import reverse
import routine

def home(request):
	if request.method == 'POST':
		form = SectionSwitchForm(request.POST)
		if form.is_valid():
			all_sections = Section.objects.all()
			current_section_id = request.POST['current_section']
			desired_section_id = request.POST['desired_section']
			student = Student(request.POST['email'], all_sections[current_section_id], all_sections[desired_section_id])
			student.save()
			return HttpResponseRedirect(reverse('thanks'))
	else:
		form = SectionSwitchForm()
	
	return render(request, "switcher/home.html", {"form": form})

def thanks(request):
	return HttpResponse("Thanks!")

		

def verify(request, hashcode):
	if routine.verify(hashcode):
		return HttpResponse("Your request has been verified!")
	else:
		return HttpResponse("Invalid verification link!")

def confirm(request, hashcode):
	if routine.confirm(hashcode):
		return HttpResponse("Your request has been confirmed!")
	else:
		return HttpResponse("Invalid confirmation link!")
