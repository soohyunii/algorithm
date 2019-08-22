# 안녕하세요, 매일프로그래밍 이번주 문제입니다.
 
# 정렬되지 않은 정수 배열과 정수 S가 주어졌을 때, 합이 S가 되는 정수 배열 내의 두 수를 찾으시오.
 
# Input: 정수 배열 = [8, 7, 2, 5, 3, 1], S = 10
# Output: 인덱스 0 과 2 (8 + 2) 또는 인덱스 1 과 4 (7 + 3)


import copy

inarray = input("int array = ")
inarray = inarray.split(',')
S = int(input("S = "))

def findSum(arr,num):
    temp = copy.deepcopy(arr)
    result = []
    switch = False
    for i in range(0, len(temp)-1, 1):
        if i > len(temp) or switch == True :
            i = 0
        temp[i] = int(temp[i])
        for j in range(1, len(temp), 1):
            temp[j] = int(temp[j])
            if (temp[i]+temp[j]) == num:
               result.append([temp[i], temp[j]])
               temp.pop(i)
               temp.pop(j-1)
               temp = temp
               switch = True
               break
            else:
                switch = False
                continue
    print ("Output : %s"%(result))


findSum(inarray,S)       
    
