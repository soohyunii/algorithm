inputint = str(input("input : "))
inputlist = []
reverselist = []

for i in range (0, len(inputint), 1) :
	inputlist.append(inputint[i])

reverselist = list(reversed(inputlist))

if inputlist == reverselist :
	print "output : True"
else :
	print "output : False"



