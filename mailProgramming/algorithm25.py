'''
안녕하세요, 매일프로그래밍 이번주 문제입니다.
 

정수 배열이 주어졌을 때, 왼쪽과 오른쪽의 합이 같은 값이 되는 위치를 찾으시오.
 
즉, A라는 배열이 있다면 A[0] + … + A[i - 1]과 A[i + 1] + … + A[n]이 같은 값이 되는 i의 위치가 답이 됩니다.
 
만약 A[1] + … + A[n]이 0이라면 0도 답이 됩니다.

Input: [0, -3, 5, -4, -2, 3, 1, 0]
Output: [0, 3, 7]
'''


inputArr = input("Input : ").split(",")
inputArr = list(map(lambda x:int(x),inputArr))


def myfunction(Array):
    output = []
    for i,v in enumerate(Array):
        if i == 0:
            leftSum = 0
            for x in range(i+1,len(Array),1):
                leftSum += Array[x]
            if leftSum == 0:
                output.append(i)
        elif i!=0 and i!= (len(Array)-1):
            leftSum = 0
            rightSum = 0
            for x in range(0,i,1):
                leftSum += Array[x]
            for x in range(i+1,len(Array),1):
                rightSum += Array[x]
            if leftSum == rightSum:
                output.append(i)
        elif i == (len(Array)-1):
            rightSum = 0
            for x in range(0,len(Array)-1,1):
                rightSum += Array[x]
            if rightSum == 0:
                output.append(i)
    return output


print(myfunction(inputArr))
    

