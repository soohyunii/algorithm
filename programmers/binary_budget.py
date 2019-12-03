import copy

def findMax(listed,Mlisted,M):
    if M < Mlisted[0]:
        return M//4
    elif M == Mlisted[0]:
        return listed[0]
    elif M > Mlisted[0] and M < Mlisted[len(Mlisted)-1]:
        temp = copy.deepcopy(Mlisted)
        temp.append(M)
        temp = sorted(temp)
        temp_index = temp.index(M)
        temp_listsum = 0
        for i in range(0,temp_index):
            temp_listsum += listed[i]
        result = (M-temp_listsum)//(len(temp)-(temp_index+1))
        return result
    else:
        return listed[len(listed)-1]

def solution(budgets, M):
    if len(budgets)<3 or len(budgets)>100000:
        print("지방의 수는 3 이상 100,000 이하인 자연수입니다.")
        return
    elif M<len(budgets) or M>1000000000:
        print("총 예산은 지방의 수 이상 1,000,000,000 이하인 자연수입니다.")
        return 
    listed_budgets = sorted(budgets)
    max_budgets =  []
    prev_sum = 0
    
    for i in range(0, len(listed_budgets)):
        if listed_budgets[i]<1 or listed_budgets[i]>100000:
            print("각 지방에서 요청하는 예산은 1 이상 100,000 이하인 자연수입니다.")
            return
        
        if i == 0 :
            element = listed_budgets[i]*len(listed_budgets)
        else :
            element = listed_budgets[i]*(len(listed_budgets)-i) + prev_sum
        prev_sum += listed_budgets[i]
        max_budgets.append(element)
    
    answer = findMax(listed_budgets,max_budgets,M)
    
    return answer

print(solution(	[120, 110, 140, 150], 485))
print(solution([100,170,165,240,200,180],1000))


'''
191203 : 여러번의 테스트 케이스 중에 하나의 실패건으로 제출을 실패했다.
어떤 조건이 빠진걸까?

'''
