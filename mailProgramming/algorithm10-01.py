# 안녕하세요, 매일프로그래밍 이번주 문제입니다.
 
# 정수 배열(int array)이 주어지면 두번째로 큰 값을 프린트하시오.

# 예제)
# Input: [10, 5, 4, 3, -1]
# Output: 5

# Input: [3, 3, 3]
# Output: Does not exist.


inarray = list(input("Input array : "))

def bubble_sort(li) :
	temp = 0
	lenarray = len(li)

	for i in range(0, lenarray, 1) :
		i = 0
		for j in range(1, lenarray, 1) :
			if li[i] > li[j] :
				temp = li[i]
				li[i] = li[j]
				li[j] = temp
			i += 1 
		lenarray -= 1
	return li

def second_max(li) :
	num = []
	result = li[len(li)-2]
	for i in range(0, len(li), 1) :
		if result == li[i] :
			num.append(result)
	if len(num) == 1 :
		print "Output : %d"%result
	elif len(num) == len(li) :
		print "Does not exist"
	else :
		print "Output(double) : %d"%result


second_max(bubble_sort(inarray))

