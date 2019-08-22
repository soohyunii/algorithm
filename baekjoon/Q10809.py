inlist = list(input("input word : "))
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
		 'r','s','t','u','v','w','x','y','z']
temp = []

for i in range(0, len(alpha), 1) :
	for j in range(0, len(inlist), 1) :
		if inlist[j] == alpha[i] :
			alpha[i] = j
			alpha[i] = int(alpha[i])
			print (alpha[i],end=' ')
			break
	if type(alpha[i]) != int :
		alpha[i] = -1
		alpha[i] = int(alpha[i])
		print (alpha[i],end=' ')




			
