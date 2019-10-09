'''
안녕하세요, 매일프로그래밍 이번주 문제입니다.

사이즈가 m인 배열 X와 사이즈가 n인 배열 Y가 주어집니다.
 
두 배열은 모두 정렬된 상태입니다.
 
배열 X에는 정확히 n개의 비어있는 셀이 있다고 할 때,
배열 Y의 원소를 X 배열로 합치며 원소들을 정렬 시키시오.
 
Input
X = [0, 2, 0, 3, 0, 5, 6, 0, 0] (비어있는 셀은 0으로 표현되었음)
Y = [1, 8, 9, 10, 15]
 
Output
X = [1, 2, 3, 5, 6, 8, 9, 10, 15]
'''


inputX = input("Input X : ").split(',')
inputY = input("Input Y : ").split(',')

def sortingX(x,y):
    isbool = False
    temp = []
    for i in range(0,len(y)):
        for j in range(0, len(x)):
            if x[j] == 0 :
                j += 1
            elif y[i] < x[j]:
                temp.append(y[i])
                y[i] = 0
                break
            elif y[i] > x[j]:
                temp.append(x[j])
                x[j] = 0
            else:
                temp.append(y[i])
                temp.append(x[j])
                y[i] = 0
                x[j] = 0
                break
            if sum(x) == 0:
                isbool = True
                break
        if (isbool == True and sum(y)!=0):
            resultY = []
            for z in range(0,len(y)):
                if y[z] != 0:
                    resultY.append(y[z])
            temp = temp + resultY
            break
    return temp

if inputX != [''] and inputY != ['']:
    inputX = list(map(lambda n:int(n), inputX))
    inputY = list(map(lambda n:int(n), inputY))
    result = sortingX(inputX,inputY)
    print(result)
else:
    print("X,Y 모두 배열을 입력해주세요")


'''
뭔가 코드가 조잡...깔끔하게 줄일 방법은 없나?
'''
