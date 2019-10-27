'''
안녕하세요, 매일프로그래밍 이번주 문제입니다.
 

정수 배열이 주어졌을 때, 배열 안에서 곱이 최대가 되는 두 정수를 찾으시오.
 
Input: [-10, -3, 5, 6, -2]
 
Output: [-10, -3] 또는 [5, 6]
'''

inputArr = input("Input : ").split(",")
inputArr = list(map(lambda n:int (n), inputArr))

def findMax(inputArr):
    outputResult = []
    result = 0

    for i in range(0, len(inputArr)):
        if inputArr[i]<0 :
            a = inputArr[i]
            for j in range(i+1,len(inputArr)):
                if inputArr[j]<0 :
                    b = inputArr[j]
                    if a*b > result :
                        result = a*b
                        if outputResult == []:
                            outputResult.append([a,b])
                        else:
                            outputResult = []
                            outputResult.append([a,b])
                    elif a*b == result :
                        outputResult.append([a,b])
        elif inputArr[i]>0 :
            a = inputArr[i]
            for z in range(i+1, len(inputArr)):
                if inputArr[z]>0 :
                    b = inputArr[z]
                    if a*b > result :
                        result = a*b
                        if outputResult == []:
                            outputResult.append([a,b])
                        else:
                            outputResult = []
                            outputResult.append([a,b])
                    elif a*b == result :
                        outputResult.append([a,b])
    return outputResult
                    
print("Output : %s"%findMax(inputArr))               
                    
