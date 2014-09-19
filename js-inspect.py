
#!/usr/bin/env python
# js-inspect.py - 2014 Roland Shoemaker
import re, argparse

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

parser = argparse.ArgumentParser(description="find stuff from a js file.")
parser.add_argument('file', help="the js file")
args = parser.parse_args()

f = open(args.file, "r")
data = f.read()
f.close()

var_funcs = re.findall(r"var (.+) = function\((.+|, .+|,.+|)\)|function (.+)\((.+|, .+|,.+|)\)|\s+(.+): function\((.+|, .+|,.+|)\)|^(?!//)\s+var (.+) = (?!function)", data, re.MULTILINE)

print(colors.HEADER+"js-inspect.py - "+args.file+colors.ENDC)
print(colors.FAIL+"[functions]"+colors.ENDC)
for i in var_funcs:
	for y in [0,2,4,6]:
		if not y == 6 and not i[y+1] == "":
			print("\t"+colors.WARNING+i[y]+colors.ENDC+"("+colors.OKBLUE+i[y+1]+colors.ENDC+")")
		elif not i[y] == "" and not y == 6:
			print("\t"+colors.WARNING+i[y]+colors.ENDC+"()")
		elif y == 6 and not i[y] == "":
			print(colors.OKGREEN+"\tvar "+i[y]+colors.ENDC)
