'''
안녕하세요, 매일프로그래밍 이번주 문제입니다.
 

크기가 n인 배열에 1부터 n-1까지의 수가 들어 있고,
중복된 수가 한 개 더 들어 있다고 할 때,
중복된 수가 무엇인지 찾으시오.
 
Input: [1, 2, 3, 4, 4]

Output: 4
 

Input: [1, 2, 3, 4, 2]

Output: 2
'''

inarray = input("Input: ").split(',')
if inarray != ['']:
    inarray = list(map(lambda n:int(n),inarray))
else:
    inarray = []

def overlap(array):
    n = len(array)
    num_sum = int(n*(n-1)/2)
    overlap_num = sum(array)-num_sum
    return overlap_num

result = overlap(inarray)
print("Output: %d"%result)


    
    
