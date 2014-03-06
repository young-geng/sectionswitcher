from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import render
from switcher.models import *
from django.core.urlresolvers import reverse
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from routine import send_verification_email
import routine

def home(request):
	return render_to_response("switcher/home.html")

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



@csrf_exempt
def thanks(request):
	if request.method == 'POST':
		if len(Course.objects.filter(code=request.POST['courses'])) == 0:
			return HttpResponse("Invalid selection!")
		c = Course.objects.get(code=request.POST['courses'])
		if len(Section.objects.filter(course=c, number=request.POST['current_sections'])) == 0:
			return HttpResponse("Invalid selection!")
		cur_sec = Section.objects.get(course=c, number=request.POST['current_sections'])
		if len(Section.objects.filter(course=c, number=request.POST['desired_sections'])) == 0:
                        return HttpResponse("Invalid selection!")
		des_sec = Section.objects.get(course=c, number=request.POST['desired_sections'])
		if len(Student.objects.filter(email=request.POST['email'])) != 0:
			return HttpResponse("Sorry, you've already registered")
		elif request.POST['current_sections'] == request.POST['desired_sections']:
			return HttpResponse("Sorry, you can't switch to the same section!")
		stu = Student()
		stu.init(request.POST['email'], cur_sec, des_sec)
		send_verification_email(request.POST['email'])
		stu.save()
		return HttpResponse("Thanks for using SectionSwap!\nA verification link has been sent to your email, please follow the instruction there!") 

@csrf_exempt
def getCourses(request):
	data_dict = {"courses": [i.code for i in Course.objects.filter(department=Department.objects.get(department=request.POST['department']))]}
	return HttpResponse(simplejson.dumps(data_dict), mimetype='application/json')

@csrf_exempt
def getSections(request):
	data_dict = {"sections": [i.number for i in Section.objects.filter(course=Course.objects.get(code=request.POST['code']))]}
	return HttpResponse(simplejson.dumps(data_dict), mimetype='application/json')


		
