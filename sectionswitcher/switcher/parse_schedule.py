from models import Department, Course, Section
import re
from sys import stdin

def parse_schedule():
    html = open("switcher/schedule.txt")
    counter = 0
    department = ""
    for line in html:
        print counter
        counter += 1
        if re.findall(r'\S+', line) == []:
            continue
        x = re.findall('([A-Z]+[\s,/&]*?[A-Z]+)\s\s+([0-9A-Z]+)\s+([\s\S]+[\S])', line)
        if x == []:
            department = line.strip()
            #print department
            #"""
            d = Department()
            d.init(department)
            d.save()
            #"""
        else:
            #print x
            code = x[0][0] + "." + x[0][1] + ".Spring.2014"
            #"""
            c = Course()
            c.init(code, d)
            c.save()
            #"""


if __name__ == '__main__':
    parse_schedule()

