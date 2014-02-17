from django.db import models

# Static Field of data

class Department(models.Model):
    department = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.department

class Course(models.Model):
    department = models.ForeignKey(Department)
    code = models.CharField(max_length = 20)

    def __unicode__(self):
        return self.code

class Section(models.Model):
    number = models.CharField(max_length = 10)
    course = models.ForeignKey(Course)

    def __unicode__(self):
        return self.number

# End of static data



class Student(models.Model):
    email = models.CharField(max_length = 100)
    current_section = models.ForeignKey(Section)
    registration_time = models.DateTimeField('registration time')

    desired_section1 = models.ForeignKey(Section)
    desired_section2 = models.ForeignKey(Section)

    verified = models.BooleanField(default = False)
    matched = models.BooleanField(default = False)







