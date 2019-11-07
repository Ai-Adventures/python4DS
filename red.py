import re 
import sys

a=''

file_name = sys.argv[1]
with open(file_name,'r') as f:
	a = re.sub(r'(Question )(\d+)',r"<span style = 'color:red'>\1\2</span>",f.read())
	print(a)
with open(file_name,'w') as f:
	f.write(a) 