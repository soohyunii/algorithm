'''
안녕하세요, 매일프로그래밍 이번주 문제입니다.
 

바이너리 배열을 주어졌을 때, 한 개의 0을 1로 바꿔 연속된 1의 수가 가장 많아지도록 하는

0의 인덱스를 찾으시오.
 
Input: [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
 
Output: 7
'''

inputR = input("input : ").split(",")
inputR = list(map(lambda n:int (n), inputR))

def mailProgramming(inputR):
    sumlist=[]
    inputlist=[]
    result=[]
    for i in range(0, len(inputR)):
        sum = 0
        if inputR[i]== 0:
            inputR[i] = 1
            for j in range(0, len(inputR)):
                if j == len(inputR)-1:
                    if inputR[j] == 1 and sum==0:
                        inputlist.append(i)
                        sumlist.append(sum)
                        inputR[i]=0
                        break
                    elif inputR[j] == 1 and sum!=0:
                        sum += 1
                        inputlist.append(i)
                        sumlist.append(sum)
                        inputR[i]=0
                    else:
                        inputR[i]=0
                        break
                elif inputR[j] == 1 and sum==0 :
                    sum += 1
                elif inputR[j] == 0 and sum!=0:
                    sumlist.append(sum)
                    inputlist.append(i)
                    sum = 0
                elif inputR[j] == 1 and sum!=0:
                    sum += 1


    for i in range(0,len(sumlist)):
        if sumlist[i] == max(sumlist):
            result.append(inputlist[i])
    return result

myresult = mailProgramming(inputR)
    
print("Output : %s"%myresult)


        
