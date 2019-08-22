# 안녕하세요, 매일프로그래밍 이번주 문제입니다. 

# 정수 배열과 정수 S가 주어졌을 때, 원소의 합이 S와 같은 가장 긴 부분 배열을 구하시오.

# 부분 배열은 배열 내의 연속된 원소들의 집합입니다.
 
# Input: [5, 6, -5, 5, 3, 5, 3, -2, 0], S = 8

# Output: [-5, 5, 3, 5]



inputlist = list(input("Input : "))
sumS = input("S = ")
templist = []
result = []

for i in range(0, len(inputlist)-1, 1) :
	listsum = inputlist[i]
	if listsum == sumS :
		templist.append(inputlist[i:i+1])
	for j in range(i+1, len(inputlist), 1) :
		listsum = listsum + inputlist[j]
		if listsum == sumS :
			templist.append(inputlist[i:j+1])

if len(templist) == 0 :
	print "Output : None"
elif len(templist) == 1 :
	print "Output : %s"%templist
else :
	maxlen = len(templist[0])
	result.append(templist[0])
	for k in range(1, len(templist), 1) :	
		if maxlen < len(templist[k]) :
			result = []
			result.append(templist[k])
			maxlen = len(templist[k])
		elif maxlen == len(templist[k]) :
			result.append(templist[k])
	print "Output : %s"%result



	
