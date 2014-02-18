from django.core.management.base import BaseCommand, CommandError
from switcher.models import *

class Command(BaseCommand):
	def handle(self, *args, **options):
		for student1 in Student.objects.all().filter(verified=True)
			for student2 in Student.objects.all().exclude(id=student1.id):
				if (isMatch(student1, student2)):
					# SEND EMAIL
					# AND OTHER STUFF


	def isMatch(student1, student1):
		return (student1.current_section.course == student2.current_section.course && student1.desired_section == student2.current_section && student2.desired_section = student1.current_section)