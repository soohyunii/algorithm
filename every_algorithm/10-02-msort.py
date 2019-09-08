def merge_sort(a):
    n = len(a)
    # 종료조건
    if n<=1 :
        return
    mid = n//2
    g1 = a[:mid]
    g2 = a[mid:]
    merge_sort(g1)
    merge_sort(g2)
    #두 그룹을 하나로 병합
    i1 = 0
    i2 = 0
    ia = 0
    while i1<len(g1) and i2<len(g2):
        if g1[i1] < g2[i2]: #이부분을 바꾸면 오름차순->내림차순
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            a[ia] = g2[i2]
            i2 += 1
            ia += 1
    #아직 남아있는 자료들을 결과에 추가
    while i1<len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2<len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1

d = [6,8,3,9,10,1,2,4,7,5]
merge_sort(d)
print(d)
            
