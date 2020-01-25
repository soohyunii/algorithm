'''
안녕하세요, 매일프로그래밍 이번주 문제입니다.
 

<<<<<<< HEAD
정수 배열이 주어졌을 때, 오른쪽 원소가 왼쪽 원소보다 더 큰 경우 중 두 원소의
차가 최대가 되는 값을 찾으시오.
 
Input: [2, 7, 9, 5, 1, 3, 5]
Output: 7 (원소 2와 9)
'''
inputArr = input("Input : ").split(",")
inputArr = list(map(lambda x:int(x), inputArr))


def maxInterval(inArr):
    temp = []
    for i,v in enumerate(inArr):
        temp.append([i,v])
    temp = sorted(temp,key=lambda temp:temp[1])
    tmax = len(temp)-1
    for i in range(tmax,-1,-1):
        for j in range(0,tmax+1):
            if temp[i][0] > temp[j][0]:
                return (temp[i][1] - temp[j][1])
        
            

print("Output : ",maxInterval(inputArr))
=======
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
        
    
>>>>>>> f8ccb38a2dcfd5a447c5b5a1c0f468bdd95dca5e
