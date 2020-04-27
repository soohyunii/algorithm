'''
안녕하세요, 매일프로그래밍 이번주 문제입니다.
 

양의 정수 배열과 정수 s가 주어졌을 때, 합이 s가 되는 원소들의 조합이 있는지
찾으시오.
 
Input: A = { 7, 3, 2, 5, 8 }, s = 14
Output: Yes (7, 2, 5)
'''

import itertools


inarr = input("Input : ").split(",")
inarr = list(map(lambda x:int(x),inarr))
innum = int(input("s = "))


def algor(inarr,innum):
    combi = []
    for i in range(1,len(inarr)+1):
        v = list(itertools.combinations(inarr,i))
        for j in range(0,len(v)):
            if sum(v[j]) == innum:
                combi.append(v[j])
    return combi

print(algor(inarr,innum))
