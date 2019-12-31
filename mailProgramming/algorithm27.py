'''
안녕하세요, 매일프로그래밍 이번주 문제입니다.
 

정수 배열이 주어졌을 때, 배열 내의 모든 0을 배열의 뒷부분으로 옮기시오.
 
단, 0을 제외한 원소들의 순서는 유지되어야 합니다.
 
Input: [6, 0, 8, 2, 3, 0, 4, 0, 1]
Output: [6, 8, 2, 3, 4, 1, 0, 0, 0]
'''

inputArr = input("Input : ").split(",")
inputArr = list(map(lambda x:int(x),inputArr))


def find_zero(Array):
    for i,v in enumerate(Array):
        j = i+1
        if v == 0 and i!=(len(Array)-1):
            while j!=len(Array):
                temp = Array[i]
                Array[i] = Array[j]
                Array[j] = temp
                j += 1
                i += 1
    print(Array)

find_zero(inputArr)
            
