from models import Department, Course, Section
import re
from sys import stdin


html = stdin
counter = 0
department = ""
for line in html:
    print counter
    counter += 1
    if re.findall(r'\S+', line) == []:
        continue
    x = re.findall('([A-Z]+[\s,/]*?[A-Z]+)\s\s+([0-9A-Z]+)\s+([\s\S]+[\S])', line)
    if x == []:
        department = line.strip()
        d = Department(department)
        d.save()
    else:
        code = x[0] + "." + x[1] + ".Spring.2014"
        c = Course(code, d)
        c.save()


