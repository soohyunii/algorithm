inarray =  list(input("Input : "))
temparray = []
outarray = []

inarray.sort()
keyarray = list(set(inarray))

for i in range(0, len(keyarray), 1) :
	if (keyarray[i] + 1) in keyarray :
		temparray.append(keyarray[i])
	elif (keyarray[i] -1) in keyarray :
		temparray.append(keyarray[i])
		temparray.append('Blind')
	else :
		temparray.append('Blind')
print temparray

for j in range(0, len(temparray), 1) :
	if (temparray[j]=='Blind') :
		for z in range :

		print outarray
		continue
	else :
		outarray.append(temparray[j])
##################stop! mistake####################
