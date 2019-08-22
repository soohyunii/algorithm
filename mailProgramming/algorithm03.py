# 안녕하세요, 매일프로그래밍 이번주 문제입니다.

# L0→L1→…→Ln-1→Ln 의 단일 연결 리스트가 주어지면 순서를 다음과 같이 바꾸시오: L0→Ln→L1→Ln-1→L2→Ln-2→…

# Given a singly linked list L: L0→L1→…→Ln-1→Ln, reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# input: 1 -> 2 -> 3 -> 4
# output: 1 -> 4 -> 2 -> 3



list01 = list(input("input list = "))

L0 = list01[0]
Ln = list01[len(list01)-1]
n = len(list01)-1

result01 = [L0,Ln]

for i in range(1,n/2+1,1):
	result01.append(list01[i])
	if i != n-i:
		result01.append(list01[n-i])
print result01
	


