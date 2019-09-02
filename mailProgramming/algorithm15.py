'''

안녕하세요, 매일프로그래밍 이번주 문제입니다.

0과 1로만 구성된 바이너리 배열이 주어졌을 때, 0과 1의 원소의 수가 같은 최대 길이의 부분 배열을 구하시오.
부분 배열은 배열 내의 연속된 원소들의 집합입니다.
Input: [0, 0, 1, 0, 1, 0, 0]
Output: [0, 1, 0, 1] 또는 [1, 0, 1, 0]

'''

inarray = input("int array = ").split(',')
inarray = list(map(lambda n: int(n), inarray))



def maxlen(list, length) :
    for i in range(length,0,-1) :
        fornum = len(list)-i*2+1
        for j in range(0, fornum) :
            result = list[j:i*2+j]
            onelen = sum(result)
            zerolen = len(result) - sum(result)
            if onelen == zerolen :
                return result
                

def compare(list) :
    onelen = sum(list)
    zerolen = len(list) - sum(list)
    
    if (len(list) < 2 or onelen == 0 or zerolen == 0) :
        print("Output : no return")
        return
    elif onelen > zerolen :
        result = maxlen(list, zerolen)
        print("Output : %s"%result)
    else :
        result = maxlen(list, onelen)
        print("Output : %s"%result)
                        

compare(inarray)
