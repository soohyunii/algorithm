'''
안녕하세요, 매일프로그래밍 이번주 문제입니다.
 

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
