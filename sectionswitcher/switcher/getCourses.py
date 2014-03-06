import sys
import json
import cgi
from models import *


fs = cgi.FieldStorage()

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")


result = {}

d = fs.getvalue(fs.keys()[0])

course_list = [i.code for i in Course.objects.filter(department=d)]

result['courses'] = course_list

sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

sys.stdout.close()