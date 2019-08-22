interList = list(input("Input (Should input [], not {}) : "))
a,b,c,d = 0,0,0,0
outList = []

for i in range(0, len(interList)-1, 1) :
	a = interList[i][1]
	b = interList[i+1][0]
	c = interList[i][0]
	d = interList[i+1][1]
	if a < b :
		if a+1 == b :
			outList.append([c,d])
		else :
			outList.append([c,a],[b,d])
	if a == b :
		outList.append([c,d])
	if a > b :
		if (c > b and d+1 == c) or (c > b and d == c) or (c > b and c+1 == d) :
			outList.append([b,a])
		elif (c < b and a > d) :
			outList.append([c,a])
		elif (c < b and a < d) or (c < b and a == d):
			outList.append([c,d])
		else :
			outList.append([b,d],[c,a])


print outList			
		





	# for j in range(0, 2, 1) :
	# 	if i != len(interList)-1 :
	# 		a = interList[i][1]
	# 		b = interList[i+1][0]
	# 	else :
	# 		a = 
	# 	print a
	# 	print b


# for idx, val in enumerate(interList):
# 	print (idx, val)


