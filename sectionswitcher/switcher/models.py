from django.db import models

# Static Field of data

class Department(models.Model):
    department = models.CharField(max_length = 100)

    def init(self, department):
        self.department = department;

    def __unicode__(self):
        return self.department

class Course(models.Model):
    department = models.ForeignKey(Department)
    code = models.CharField(max_length = 20)

    def init(self, code, department):
        self.code = code
        self.department = department

    def __unicode__(self):
        return self.code

class Section(models.Model):
    number = models.CharField(max_length = 10)
    course = models.ForeignKey(Course)

    def init(self, number, course):
        self.number = number
        self.course = course

    def __unicode__(self):
        return self.number

# End of static data



class Student(models.Model):
    email = models.CharField(max_length = 100)
    current_section = models.ForeignKey(Section, related_name='current_section')
    registration_time = models.DateTimeField('registration time')

    desired_section = models.ForeignKey(Section, related_name='desired_section')

    verified = models.BooleanField(default = False)
    confirmed = models.BooleanField(default = False)

class PendingMatch(models.Model):
    student1 = models.ForeignKey(Student, related_name='student1')
    student2 = models.ForeignKey(Student, related_name='student2')

    matched = models.DateTimeField(auto_now_add=True)







