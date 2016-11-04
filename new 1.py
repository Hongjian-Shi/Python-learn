import re

name = raw_input('Enter file name:')
fh = open(name)

Num = []
for line in fh:
	if re.search('[0-9]+',line):
		num = re.findall('[0-9]+',line)
		for number in num:
			Num.append(number)

sum = int()
for number in Num:
	number = int(number)
	sum = number + sum

print sum