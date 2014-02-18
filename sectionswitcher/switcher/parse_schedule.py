import re
html = open("schedule.txt")

for line in html:
    if re.findall('[0-9]+', line) == []:
        continue
    print re.findall('([A-Z]+[\s,/]*?[A-Z]+)\s\s+([0-9A-Z]+)\s+([\s\S]+[\S])', line)
