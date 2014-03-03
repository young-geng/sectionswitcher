from sys import stdin, stdout
from models import *
from datetime import datetime, timedelta



def expire_varification():
    varifying_students = Student.objects.filter(varified=False)
    for student in varifying_students:
        t = datetime.now() - student.registration_time
        if t.total_seconds() > 12 * 60 * 60:
            t.delete()


def expire_match():
    matches = Match.objects.all()
    for match in matches:
        if match.student1.confirmed and match.student2.confirmed:
            pass # FIXME send email
        elif (datetime.now() - match.match_time).total_seconds() > 22 * 60 * 60: # Expired
            if not match.student1.confirmed:
                match.student1.delete()
            else:
                match.student1.matched = False
                match.student1.confirmed = False
                match.student1.save()
                pass # FIXME send email to student1
            if not match.student2.confirmed:
                match.student2.delete()
            else:
                match.student2.matched = False
                match.student2.confirmed = False
                match.student2.save()
                pass # FIXME send email to student1
        match.delete()


def find_match():
    students = Student.objects.filter(varified=True, matched=False).order_by('registration_time')
    for i in range(len(students)):
        for j in range(i + 1, len(students)):
            if not student[i].matched and not student[j].matched:
                if students[i].current_section == student[j].desired_section and student[i].desired_section == student[j].current_section:
                    m = Match()
                    m.init(student[i], student[j], datetime.now())
                    m.save()
                    student[i].matched = True
                    student[j].matched = True
                    student[i].save()
                    student[j].save()
                    pass # FIXME send email





        