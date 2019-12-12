'''
안녕하세요, 매일프로그래밍 이번주 문제입니다.
 
정수 배열이 주어졌을 때, 짝수 위치의 원소가 양 옆의 원소보다 큰 수가 되도록 배치하시오.

배열에는 중복 원소가 없다고 가정합니다.

 

Input: [1, 2, 3, 4, 5, 6, 7]

Output: [1, 3, 2, 5, 4, 7, 6]

 

Input: [9, 6, 8, 3, 7]

Output: [6, 9, 3, 8, 7]

 

Input: [6, 9, 2, 5, 1, 4]

Output: [6, 9, 2, 5, 1, 4]
'''


inputAr = input("Input : ").split(",")
inputAr = list(map(lambda n:int(n), inputAr))


def algorithm(inputArray):
    for i,v in enumerate(inputArray):
        i = i+1
        if i%2 == 0:
            if inputArray[i-1] < inputArray[i-2]:
                temp = inputArray[i-1]
                inputArray[i-1] = inputArray[i-2]
                inputArray[i-2] = temp
            if i!=len(inputArray) and inputArray[i-1] < inputArray[i]:
                temp = inputArray[i-1]
                inputArray[i-1] = inputArray[i]
                inputArray[i] = temp
    return inputArray



print(algorithm(inputAr))
