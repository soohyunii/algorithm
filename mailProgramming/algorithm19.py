'''
안녕하세요, 매일프로그래밍 이번주 문제입니다.
 

원소가 0, 1, 2로 구성된 배열이 주어졌을 때, 상수 공간을 이용해 선형 시간에 배열을 정렬하시오.
 
Input: [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
 
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2]
'''

inlist = input("Input: ").split(',')

def sorting(input_list):
    zero = []
    one = []
    two = []
    isEnd = False

    if (input_list != ['']) :
        input_list = list(map(lambda n:int(n), input_list))
    else :
        print("Please input number list")
        return False
    
    for i in range(0,len(input_list)):
        if input_list[i] == 0 :
            zero.append(0)
        elif input_list[i] == 1 :
            one.append(1)
        elif input_list[i] == 2 :
            two.append(2)
        else :
            print("Only 0,1,2 accepted. Please input number list")
            isEnd = True
            break
    if isEnd == True :
        return False
    result = zero + one + two
    print("Output: %s"%result)
    return result

sorting(inlist)
    

