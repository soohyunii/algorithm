'''
안녕하세요, 매일프로그래밍 이번주 문제입니다.
 

M x N 크기의 양의 정수 매트릭스와 비용(cost)가 주어졌을 때,
주어진 비용으로 매트릭스의 시작 위치 (0, 0)에서 마지막 위치 (M-1, N-1)까지
도달하는 경로의 수를 구하시오.
 
매트릭스에서 이동한 경로의 비용은 거쳐간 셀 값의 합이다.
 
매트릭스에서는 오직 오른쪽 한 칸 또는 아래쪽 한 칸으로만 이동할 수 있다.
 
즉, 셀 (i, j)에서는 (i, j+1) 또는 (i+1, j)로 이동할 수 있다.
 
Input: mat =  [[4, 7, 1, 6]
              ,[5, 7, 3, 9]
              ,[3, 2, 1, 2]
              ,[7, 1, 6, 3]]
 cost = 25
Output: 2 (두 가지 경로는 4-7-1-3-1-6-3, 4-5-7-3-1-2-3)
'''

def algor(mat,cost):
    #start = mat[0][0]
    #end = mat[len(mat)-1][len(mat[0])-1]
    #sum = []

    #sum.append(start)
    
    matrix = {}
    sumArr = []
    loadArr = [] 

    sumArr.append(mat[0][0])
    loadArr.append((0,0))

    for i in range(0,len(mat)):
        for j in range(0,len(mat[0])):
            if i == len(mat)-1 and j == len(mat[0])-1:
                matrix[i,j] = [0,0]
            elif i == len(mat)-1:
                matrix[i,j] = [0,mat[i][j+1]]
            elif j == len(mat[0])-1:
                matrix[i,j] = [mat[i+1][j],0]
            else:
                matrix[i,j] = [mat[i+1][j],mat[i][j+1]]
    return matrix
    '''
    while sumArr:
        p = loadArr.pop(0)
        v = p[-1]
        if sum[sumArr]>cost:
            print()
    '''     
    

mat =  [[4, 7, 1, 6]
              ,[5, 7, 3, 9]
              ,[3, 2, 1, 2]
              ,[7, 1, 6, 3]]
print(algor(mat,25))

    

'''
    matrix=딕셔너리에 각 원소의 (i, j+1) , (i+1, j) 값을 입력한다.
    ex) {4: [7, 5], 7: [1, 7]}
    이런식으로 matrix를 완성하면 모두의 알고리즘에서 배웠던 미로찾기 공식을
    이용해서 푼다.
    
'''
        

'''

    if (len(mat)-1) > (len(mat[0])-1):
        max = len(mat)-1
    elif (len(mat)-1) < (len(mat[0])-1):
        max = len(mat[0])-1
    else:
        max = len(mat[0])-1

    for i in range(0,max):
        while sum<cost:
            
        
'''
    

    
        
        
        
            
        
