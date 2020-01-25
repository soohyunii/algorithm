'''
정수 배열이 주어졌을 때, 합이 최대가 되는 부분 배열을 찾아 출력하시오.
 
단, 부분 배열의 원소들은 연속된 원소들로 구성되어야 합니다.
 
Input: [-2, 1, -3, 4, -1, 2, 1, -5, -4]
Output: [4, -1, 2, 1]
 
Input: [8, -7, -3, 5, 6, -2, 3, -4, 2]
Output: [5, 6, -2, 3]

'''

inArray = input("Input : ").split(",")
inArray = list(map(lambda x:int(x),inArray))


def solution(inarray):
    maxValue = inarray[0]
    maxArray = []
    maxArray.append(maxValue)
    j = 1
    while j < len(inarray):
        for i in range(0,len(inarray)-j):
            tempList = []
            temp = 0
            for i in range(i,i+j):
                tempList.append(inarray[i])
                temp += inarray[i]
            if maxValue < temp:
                maxValue = temp
                maxArray = tempList
        j+=1
    return maxArray



print("Output : ",solution(inArray))
    
