# 안녕하세요, 매일프로그래밍 이번주 문제입니다.
 
# 간격(interval)로 이루어진 배열이 주어지면, 겹치는 간격 원소들을 합친 새로운 배열을 만드시오. 간격은 시작과 끝으로 이루어져 있으며 시작은 끝보다 작거나 같습니다.
 
# 예제)
# Input: {{2,4}, {1,5}, {7,9}}
# Output: {{1,5}, {7,9}}

# Input: {{3,6}, {1,3}, {2,4}}
# Output: {{1,6}}


import copy

inlist = list(input("Input (Should input [], not {}) : "))

def sorting(list) :
	list.sort()

def compare(list) :
	sorting(list)
	lenlist = len(list)
	for i in range(0, lenlist, 1) :
		if i < lenlist-1 :
			a = list[i][0]
			b = list[i][1]
			c = list[i+1][0]
			d = list[i+1][1]
			if b >= d :
				list.remove([c,d])
				lenlist-=1 
			elif b < d and b >= c :
				list.remove([a,b])
				list.remove([c,d])
				list.insert(0,[a,d])
				lenlist-=1
		if i == lenlist :
			print "Output : %s"%list

compare(inlist)


# 단점 : 결과가 나오기 까지의 단계 배열들도 출력됨