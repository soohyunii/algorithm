inarray = list(input("Input array : "))
standard = 0
output = []

# find second max 
for i in range(0, len(inarray), 1) :
	a = 0
	b = 0
	standard = inarray[i]
	for j in range(0, len(inarray), 1) :
		if standard < inarray[j] :
			a += 1
		if standard == inarray[j] :
			b += 1
	if a == 1 and b == 0:
		output.append(standard)
	elif a == 1 and b != 0:
		output.append(standard)
		output = list(set(output))
	elif a == 0 and b != 0:
		output.append('Does not exist')
		output = list(set(output))
	else:
		output.append('')
print "Output : %s"%output

#######################mistake!###################



