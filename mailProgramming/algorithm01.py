
# 안녕하세요, 매일프로그래밍 이번주 문제입니다.
 

# 랜덤한 정수 배열이 주어지면 중복된 원소의 값을 모두 프린트 하시오. 단, 공간복잡도 O(1)이여야 합니다.
# Given an integer array, print all non unique elements.

# input: [0, 6, 3, 4, 0]
# output: 0

# input: [5, 4, 3, 2, 1, 1, 1, 1, 1, 2]
# output: 1, 2

a = []
b = input()
c = 0 
out = []

for i in range(0, len(b), 1):
	a.append(b[i])
	if len(a) > 1 :
		c = a[i]
		for j in range(0, len(a)-1, 1):
			if c == a[j] :
				if c in out :
					continue
				else :
					out.append(c)
					continue
			else :
				continue
				# twice for syntax : 'continue' goes upmost (first for syntax) 'for..in..' 
	else :
		continue
print "output : %s" % out





