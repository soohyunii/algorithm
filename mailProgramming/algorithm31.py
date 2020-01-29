'''
안녕하세요, 매일프로그래밍 이번주 문제입니다.
 

양의 정수 배열과 정수 s가 주어졌을 때, 합이 s가 되는 원소들의 조합이 있는지
찾으시오.
 
Input: A = { 7, 3, 2, 5, 8 }, s = 14
Output: Yes (7, 2, 5)
'''

inarr =  input("Input : ").split(",")
inarr =  list(map(lambda x:int(x),inarr))
inum =  int(input("s : "))

def findS(arr,s):
    minum = min(arr)
    snum = sum(arr)
    if minum > s :
        return "No, s is less than min"
    elif snum < s :
        return "No, s is more than sum"
    else :
        tempArr = sorted(arr, reverse=True)
        def recursive(len(tempArr)):
            if s == 0 :
                return "Yes"
            elif s < minum :
                
            
                    



print(findS(inarr,inum))
