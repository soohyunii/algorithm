'''
안녕하세요, 매일프로그래밍 이번주 문제입니다.
 

바이너리 배열(원소를 0, 1만 갖는 배열)이 주어졌을 때, 배열을 정렬하시오.

단, 시간 복잡도는 O(n), 공간 복잡도는 O(1).

결과는 0이 먼저 출력되고 1이 출력되어야 합니다.
 
Input: [1, 0, 1, 0, 1, 0, 0, 1]

Output: [0, 0, 0, 0, 1, 1, 1, 1]
'''


inarray = input("Input : ").split(',')
if inarray != ['']:
    inarray = list(map(lambda n : int(n), inarray))
else:
    inarray = []


def binary_sort(array):
    zero = []
    one = []
    result = []

    for i in range(0,len(array)):
        if array[i] == 0:
            zero.append(array[i])
        elif array[i] == 1:
            one.append(array[i])
        else:
            return
    result = zero+one
    return result


print(binary_sort(inarray))


