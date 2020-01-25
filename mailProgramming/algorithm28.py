'''
안녕하세요, 매일프로그래밍 이번주 문제입니다.
 

정수 배열이 주어졌을 때, 합이 최대가 되는 부분 배열을 찾아 출력하시오.
 
단, 부분 배열의 원소들은 연속된 원소들로 구성되어야 합니다.
 
Input: [-2, 1, -3, 4, -1, 2, 1, -5, -4]
Output: [4, -1, 2, 1]
 
Input: [8, -7, -3, 5, 6, -2, 3, -4, 2]
Output: [5, 6, -2, 3]
'''

def findMaxSum(Array):
    i = 0
    maxsum = 0
    tsum = 0
    while i<len(Array):
        for x in range(0,len(Array)):
            for t in range(x,i):
                tsum += Array[t]
                if tsum > maxsum:
                    maxsum = tsum
        i=i+1
    print(maxsum)

findMaxSum([1,2,3,4,5,6])
