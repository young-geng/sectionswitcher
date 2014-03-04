from sys import stdin, stdout
from models import *
from datetime import datetime, timedelta



def expire_verification():
    verifying_students = Student.objects.filter(verified=False)
    for student in verifying_students:
        t = datetime.today() - student.registration_time
        if t.total_seconds() > 12 * 60 * 60:
            student.delete()


def expire_match():
    matches = PendingMatch.objects.all()
    for match in matches:
        print (datetime.today() - match.match_time).total_seconds()
        if match.student1.confirmed and match.student2.confirmed:
            pass # FIXME send email
            match.delete()
        elif (datetime.today() - match.match_time).total_seconds() > 22 * 60 * 60: # Expired
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
    students = Student.objects.filter(verified=True, matched=False).order_by('registration_time')
    for i in range(len(students)):
        for j in range(i + 1, len(students)):
            if not students[i].matched and not students[j].matched:
                if students[i].current_section == students[j].desired_section and students[i].desired_section == students[j].current_section:
                    m = PendingMatch()
                    m.init(students[i], students[j])
                    m.save()
                    students[i].matched = True
                    students[j].matched = True
                    students[i].save()
                    students[j].save()
                    pass # FIXME send email





        