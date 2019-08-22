# 안녕하세요, 매일프로그래밍 이번주 문제입니다.
 
# 정수 배열(int array)이 주어지면 0이 아닌 정수 순서를 유지하며 모든 0을 배열 오른쪽 끝으로 옮기시오. 단, 시간복잡도는 O(n), 공간복잡도는 O(1)여야 합니다.

# 예제)
# Input: [0, 5, 0, 3, -1]
# Output: [5, 3, -1, 0, 0]

# Input: [3, 0, 3]
# Output: [3, 3, 0]


import copy

inputarray = list(input("Input : "))
zeroarray = []
numarray = copy.deepcopy(inputarray)

for i in range(0, len(inputarray), 1) :
	if inputarray[i] == 0 :
		zeroarray.append(inputarray[i])
		numarray.remove(0)

outarray = numarray + zeroarray
print outarray



