from models import Department, Course, Section
from urllib2 import urlopen
import json




def get_sections():
    total_c = 0
    total_s = 0
    courses = Course.objects.all()
    for course in courses:
        total_s += 1
        try:
            link = "https://apis-dev.berkeley.edu/cxf/asws/classoffering/" + course.code + "?_type=json&app_id=a641ceca&app_key=eea0330432f77b498709afe6fe7fb6f8"
            data = json.loads(urlopen(link).read())
            sections = data["ClassOffering"]["sections"]
            if type(sections) == list:
                for section in sections:
                    total_c += 1
                    number = section['sectionNumber']
                    s = Section()
                    s.init(number, course)
                    s.save()
            elif type(sections) == dict:
                total_c += 1
                number = sections['sectionNumber']
                s = Section()
                s.init(number, course)
                s.save()
        except Exception:
            continue
        print "Courses:   " + str(total_s) + " / " + str(len(courses)) + "     Sections:   " + str(total_c)    
if __name__ == '__main__':
    get_sections()

