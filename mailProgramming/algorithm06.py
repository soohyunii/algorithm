# 안녕하세요, 매일프로그래밍 이번주 문제입니다.
 
# 1~N 까지 있는 정수 배열에 원소 하나가 없어졌습니다. 없어진 원소의 값을 구하시오.

# Given an integer array of 1~N except one number, find the missing integer.


numlist = list(input("1~N num list input : "))
num = 0

for i in range(0, len(numlist), 1):
	num = numlist[i]
	if num != i+1 :
		print "missing number is : %d" %(num-1)
		break
	elif num == len(numlist) :
		print "maybe..missing number is : %d" %(num+1)

