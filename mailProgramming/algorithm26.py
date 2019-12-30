'''
안녕하세요, 매일프로그래밍 이번주 문제입니다.
 

중복된 원소가 있는 정수 배열이 주어졌을 때, 주요 원소를 찾으시오.
 
주요 원소는 배열 크기의 반을 초과하여 등장하는 원소입니다.
 
Input: [2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]
Output: 2
'''

inputArr = input("Input : ").split(",")
inputArr = list(map(lambda x:int(x), inputArr))


def findMain(inputArr):
    for i in range(0,len(inputArr)):
        if i == 0:
            temp = {inputArr[i]:1}
        else:
            if inputArr[i] not in temp:
                temp[inputArr[i]]=1
            else:
                temp[inputArr[i]]+=1
    for key in temp:
        if temp[key] > (len(inputArr)//2):
            return "Output : %d"%key
            

print(findMain(inputArr))


