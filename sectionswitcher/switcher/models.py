from django.db import models
from datetime import datetime
from django import forms

# Static Field of data

class Department(models.Model):
    department = models.CharField(max_length = 100)

    def init(self, department):
        self.department = department;

    def __unicode__(self):
        return self.department

    def equals(self, departmen):
        return self.department == department

class Course(models.Model):
    department = models.ForeignKey(Department)
    code = models.CharField(max_length = 20)

    def init(self, code, department):
        self.code = code
        self.department = department

    def __unicode__(self):
        return self.code

    def equals(self, course):
        return self.code ==  course.code

class Section(models.Model):
    number = models.CharField(max_length = 10)
    course = models.ForeignKey(Course)

    def init(self, number, course):
        self.number = number
        self.course = course

    def __unicode__(self):
        return self.number

    def equals(self, section):
        return self.number == section.number and self.course.equals(section.course)

# End of static data



class Student(models.Model):
    email = models.CharField(max_length = 100)
    current_section = models.ForeignKey(Section, related_name='current_section')
    registration_time = models.DateTimeField('registration time')

    desired_section = models.ForeignKey(Section, related_name='desired_section')

    verified = models.BooleanField(default = False)
    matched = models.BooleanField(default = False)
    confirmed = models.BooleanField(default = False)

    def init(
            self, email, current_section, desired_section, 
            registration_time=datetime.today(), verified=False,
            matched=False, confirmed=False):
        self.email = email
        self.current_section = current_section
        self.desired_section = desired_section
        self.registration_time = registration_time
        self.verified = verified
        self.matched = matched
        self.confirmed = confirmed


    def __unicode__(self):
        return "Email: " + str(self.email) + " | current_sec: " + str(self.current_section)\
            + " | desired_sec: " + str(self.desired_section) + " | verified: " + str(self.verified)\
            + " | matched: " + str(self.matched) + " | confirmed: " + str(self.confirmed) + "\n" 


class PendingMatch(models.Model):
    student1 = models.ForeignKey(Student, related_name='student1')
    student2 = models.ForeignKey(Student, related_name='student2')

    match_time = models.DateTimeField(auto_now_add=True)

    def init(self, student1, student2, match_time=datetime.today()):
        self.student1 = student1
        self.student2 = student2
        self.match_time = match_time

    def __unicode__(self):
        return "Match between: " + self.student1.email + "  " + self.student2.email + "\n"

class SectionSwitchForm(forms.Form):
    email = forms.EmailField(max_length=50);
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    current_section = forms.ModelChoiceField(queryset=Section.objects.all())
    desired_section = forms.ModelChoiceField(queryset=Section.objects.all())


