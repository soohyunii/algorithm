# 안녕하세요, 매일프로그래밍 이번주 문제입니다.
 
# 정수 배열이 주어졌을 때, 중복된 값이 들어 있지 않고 연속된 정수로 구성된 가장 긴 부분 배열을 구하시오.
# 부분 배열은 배열 내의 연속된 원소들의 집합입니다.
 
# Input: [2, 0 , 2, 1, 4, 3, 1, 0]

# Output: [0, 2, 1, 4, 3]


inarray =  list(input("Input : "))
temparray = []
lenarray = []
outarray = []
breaker = False
a = 0

for i in range(0, len(inarray)-1, 1) :
	if breaker == False :
		temparray.append(inarray[i])
	for j in range(i+1, len(inarray), 1) :
		if inarray[j] in temparray :
			if len(temparray) > a :
				outarray = []
				outarray.append(temparray)
				lenarray.append(len(temparray))
				a = max(lenarray)
				temparray = []
			elif len(temparray) == a:
				outarray.append(temparray)
				breaker = True
				break
			else :
				temparray = []
			break
		else :
			temparray.append(inarray[j])
		if j == len(inarray)-1 :
			if len(temparray) == a :
				outarray.append(temparray)
			elif len(temparray) > a :
				outarray = temparray
			breaker = True
			break
	if breaker == True :
		break
print "Output : %s"%outarray


