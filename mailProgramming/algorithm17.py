'''
안녕하세요, 매일프로그래밍 이번주 문제입니다.
 
두 개의 정렬된 배열 X, Y가 주어졌을 때,
두 배열의 크기를 유지하면서 두 배열의 전체를 정렬하시오.
 
즉, 배열 X에는 작은 수들로 배열 Y에는 큰 수들로 구성되고
원소들은 정렬되어 있어야 합니다.
 
단, 정렬 시 다른 자료 구조를 사용하지 않고 주어진 배열만을 이용해야 합니다.
 
Input
X: [1, 4, 7, 8, 10]
Y: [2, 3, 9]
 
Output
X: [1, 2, 3, 4, 7]
Y: [8, 9, 10]
'''
'''
1. 간단한 방식
: 두 배열을 합친다 -> 하나가 된 배열을 정렬 -> len(x)만큼 자름

2. 좀 더 복잡한 방식
: 두 배열의 첫째 원소끼리 비교. 만약 Y에 있는 원소가 더 작다면 X원소와 교환
-> Y원소는 모든 X원소와 한번씩 비교해야 한다. 
-> 만약 Y원소에서 X와 바꾸지 않은 원소가 있다면  이미 X는 배열된 것이므로 그 뒤의 Y 원소는 비교할 필요가 없다.
-> Y 배열만 다시 순서대로 정렬하고 X,Y를 리턴

두번째 방식으로 풀어볼것이다.
'''

inputX = input("Input X : ").split(',')
inputY = input("Input Y : ").split(',')

def myArray_Y(a):
    for i in range(0, len(a)-1):
        if a[i] > a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
    return a


def myArray(a,b):
    switch = False
    for i in range(0, len(b)):
        for j in range(0, len(a)):
            last = len(a)-1
            if a[last] < b[i]:
                switch = True
                break
            if a[j] > b[i]:
                temp = a[j]
                a[j] = b[i]
                b[i] = temp
        if switch == True:
            break
    myArray_Y(b)
    return a,b


if inputX != [''] and inputY != ['']:
    inputX = list(map(lambda n:int(n), inputX))
    inputY = list(map(lambda n:int(n), inputY))
    result = myArray(inputX,inputY)
    print(result)
else:
    print("X,Y 모두 배열을 입력해주세요")
    


    
