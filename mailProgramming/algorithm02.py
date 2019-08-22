# 안녕하세요, 매일프로그래밍 이번주 문제입니다.
# 정수 배열과 정수 K가 주어지면 원소 3개의 합으로 K가 만들어지는지 체크하시오.

# Given an integer array and an integer K, check if sum of 3 elements from the array equals to K.


aa = list(input("Please input integer list : "))
k = int(input("Please input integer sum : "))

# int var 3num
v1,v2,v3 = 0,0,0

for i in range(0,len(aa),1):
	v1 = aa[i]
	for j in range(i+1,len(aa),1):
		v2 = aa[j]
		v3 = k - v1 - v2
		if v3 in aa :
			print "true : %d, %d, %d" % (v1,v2,v3)
		break
	break




