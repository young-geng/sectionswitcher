"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from switcher.models import Department, Course, Section, Student, PendingMatch
import routine
from datetime import datetime





""" Test for Model Department, Course and Section """
class SectionDataTest(TestCase):


    def setUp(self):
        d = Department()
        d.init("CS")
        d.save()
        c = Course()
        c.init("CS61C", d)
        c.save()
        s = Section()
        s.init("101", c)
        s.save()
        s = Section()
        s.init("102", c)
        s.save()


    """ Test if all departments have at lease one course """
    def test_departments(self):
        departments = list(Department.objects.all())
        for course in Course.objects.all():
            if course.department in departments:
                departments.remove(course.department)
        self.assertTrue(len(departments) == 0, "Some departments have no courses")

    """ Test if all courses have at lease one section """
    def test_courses(self):
        courses = list(Course.objects.all())
        for section in Section.objects.all():
            if section.course in courses:
                courses.remove(section.course)
        self.assertTrue(len(courses) == 0, "Some courses have no sections")





""" Test for Model Student """
class StudentTest(TestCase):


    def setUp(self):
        d = Department()
        d.init("CS")
        d.save()
        c = Course()
        c.init("CS61C", d)
        c.save()
        s = Section()
        s.init("101", c)
        s.save()
        s = Section()
        s.init("102", c)
        s.save()
        sections = Section.objects.all()
        sec1 = sections[0]
        sec2 = sections[1]
        stu1 = Student()
        stu1.init("student1@example.com", sec1, sec2, verified=True)
        stu2 = Student()
        stu2.init("student2@example.com", sec2, sec1, verified=True)
        stu1.save()
        stu2.save()

    """ Create student test """
    def test_student_create(self):
        sections = Section.objects.all()
        sec1 = sections[0]
        sec2 = sections[1]
        stu1 = Student.objects.filter(email="student1@example.com")[0]
        stu2 = Student.objects.filter(email="student2@example.com")[0]

        self.assertTrue(
                stu1.current_section == sec1 and
                stu1.desired_section == sec2 and
                stu2.current_section == sec2 and
                stu2.desired_section == sec1,
                "Student information retrieved is incorrect")



    """ Test for find_match routine """
    def test_find_match(self):
        stu1 = Student.objects.filter(email="student1@example.com")[0]
        stu2 = Student.objects.filter(email="student2@example.com")[0]
        stu1.verified = True
        stu2.verified = True
        stu1.save()
        stu2.save()
        routine.find_match()
        stu1 = Student.objects.filter(email="student1@example.com")[0]
        stu2 = Student.objects.filter(email="student2@example.com")[0]
        print stu1, stu2
        print len(PendingMatch.objects.all())
        self.assertTrue(len(PendingMatch.objects.all()) == 1, "Wrong match")
        print PendingMatch.objects.all()[0]
        print stu1, stu2
        self.assertTrue(stu1.matched and stu2.matched, "Student matched flag not set")



    """ Test for expire_verifying routine """
    def test_expire_verification(self):
        stu1 = Student.objects.filter(email="student1@example.com")[0]
        stu2 = Student.objects.filter(email="student2@example.com")[0]
        stu1.verified = False
        stu1.registration_time = datetime(2014, 3, 1)
        stu1.save()
        routine.find_match()
        self.assertTrue(len(PendingMatch.objects.all()) == 0, "Wrong match")
        routine.expire_verification()
        self.assertTrue(len(Student.objects.all()) == 1, "Student not expired!")
