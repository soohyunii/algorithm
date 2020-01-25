import copy

def findMax(listed,Mlisted,M):
    temp = []
    if M < Mlisted[0]:
        return M//len(listed)
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
    listed_budgets = sorted(budgets)
    max_budgets =  []
    prev_sum = 0

    for i in range(0, len(listed_budgets)):
        if i == 0 :
            element = listed_budgets[i]*len(listed_budgets)
        else :
            element = listed_budgets[i]*(len(listed_budgets)-i) + prev_sum
        prev_sum += listed_budgets[i]
        max_budgets.append(element)

    answer = findMax(listed_budgets,max_budgets,M)

    return answer

print(solution( [120, 110, 140, 150], 485))
print(solution([100, 200, 170, 165, 180, 240],200))
