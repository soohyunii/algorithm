def bubble_sort_sub(a,end):
    if end <= 0 :
        return a
    for i in range(0,end-1):
        if a[i]>a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
    bubble_sort_sub(a,end-1)
    


def bubble_sort(a):
    return bubble_sort_sub(a,len(a)-1)


d = [6,4,1,3,2,5]
bubble_sort(d)
print(d)
