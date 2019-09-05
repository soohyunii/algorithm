'''
안녕하세요, 매일프로그래밍 이번주 문제입니다.
 

정수 배열이 주어졌을때, 합이 0이 되는 모든 부분 배열을 출력하시오.

부분 배열은 배열 내의 연속된 원소들의 집합입니다.
 
Input: [4, 2, -3, -1, 0, 4]

Output:
[-3, -1, 0, 4]
[0]
 

Input: [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

Output:
[3, 4, -7]
[4, -7, 3]
[-7, 3, 1, 3]
[3, 1, -4]
[3, 1, 3, 1, -4, -2, -2]
[3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

'''
import copy

inlist = input("Input : ").split(',')
inlist = list(map(lambda n: int(n), inlist))

def iszero(list) :
    if sum(list) == 0 :
        return list

def sort(list) :
    temp = []
    final = []
    for i in range(0, len(list)) :
        temp.append(list[i])
        a = copy.deepcopy(iszero(temp))
        if a != None :
            final.append(a)
        for j in range(i+1, len(list)) :
            temp.append(list[j])
            b = copy.deepcopy(iszero(temp))
            if b != None :
                final.append(b)
        temp = []
    print("Output : ")
    for z in range(0, len(final)) :
        print(final[z],sep='\n')

sort(inlist)


# 위의 for문을 람다로 바꿀 수 있을까?









