from sys import stdin, stdout
from models import *
from datetime import datetime, timedelta
from hashlib import md5
import smtplib



def expire_verification():
    verifying_students = Student.objects.filter(verified=False)
    for student in verifying_students:
        t = datetime.today() - student.registration_time
        if t.total_seconds() > 12 * 60 * 60:
            student.delete()


def expire_match():
    matches = PendingMatch.objects.all()
    for match in matches:
        #print (datetime.today() - match.match_time).total_seconds()
        if match.student1.confirmed and match.student2.confirmed:
            send_match_completed_email(match.student1.email, match.student2.email)
            match.student1.delete()
            match.student2.delete()
            match.delete()
        elif (datetime.today() - match.match_time).total_seconds() > 22 * 60 * 60: # Expired
            if not match.student1.confirmed:
                match.student1.delete()
            else:
                match.student1.matched = False
                match.student1.confirmed = False
                match.student1.save()
                send_match_cancelled_email(match.student1.email)
            if not match.student2.confirmed:
                match.student2.delete()
            else:
                match.student2.matched = False
                match.student2.confirmed = False
                match.student2.save()
                send_match_cancelled_email(match.student2.email)
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
                    send_confirmation_email(students[i].email)
                    send_confirmation_email(students[j].email)



def hash(text):
    return md5(text + "ail(*#Cn03f09zx-_(").hexdigest()



def verify(code):
    students = Student.objects.filter(verified=False)
    for i in students:
        if hash(i.email) == code:
            i.verified = True
            i.save()
            return True
    return False

def confirm(code):
    students = Student.objects.filter(verified=True, matched=True)
    for i in students:
        if hash(i.email) == code:
            i.confirmed = True
            i.save()
            return True
    return False






def send_verification_email(address):
    link = "http://CalSectionSwitcher.io/varify/" + hash(address)
    message = \
    """
    Hi,

    Thanks for using CalSectionSwitcher!
    Please click the following link to confirmed your request.
    %s

    Regards,
    CalSectionSwitcher Team
    """ % link
    send_email(address, message)


def send_confirmation_email(address):
    link = "http://CalSectionSwitcher.io/confirm/" + hash(address)
    message = \
    """
    Hi,

    Thanks for using CalSectionSwitcher!
    The system automatically found a match for you! Please click the following link to confirm.
    %s

    Regards,
    CalSectionSwitcher Team
    """ % link
    send_email(address, message)

def send_match_canceled_email(address):
    message = \
    """
    Hi,

    Thanks for using CalSectionSwitcher!
    We are sorry that your match is cancelled because the student who matches you hasn't respond to us.
    Your request will be put back into the system to continue matching.


    Regards,
    CalSectionSwitcher Team
    """ % link
    send_email(address, message)     


def send_match_completed_email(address1, address2):
    message = \
    """
    Hi,

    Thanks for using CalSectionSwitcher!
    We are here to tell you the contact of the person who matches you.
    His / Her email address is %s


    Regards,
    CalSectionSwitcher Team
    """ % address1
    send_email(address2, message)
    message = \
    """
    Hi,

    Thanks for using CalSectionSwitcher!
    We are here to tell you the contact of the person who matches you.
    His / Her email address is %s


    Regards,
    CalSectionSwitcher Team
    """ % address2
    send_email(address1, message)




def send_email(address, text):  
  
    fromaddr = 'calsectionswitcher@gmail.com'  
    subject = 'CalSectionSwitcher Notification' 

    msg = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (fromaddr, address, subject, text)
    msg = text
      
    # Credentials (if needed)  
    username = 'calsectionswitcher'  
    password = 'byebye123'
     
    failure = 0 
    # The actual mail send 
    while failure < 5:
        try: 
            server = smtplib.SMTP('smtp.gmail.com:587')  
            server.starttls()  
            server.login(username,password)  
            server.sendmail(fromaddr, address, msg)  
            server.quit()
            break
        except Exception as e:
            failure += 1

