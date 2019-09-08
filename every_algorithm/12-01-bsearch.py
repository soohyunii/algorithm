def binary_search(a,x):
    start = 0
    end = len(a)-1

    while start<=end:
        mid = (start+end)//2
        if x == a[mid] :
            return mid
        elif x < a[mid] :
            end = mid-1
        else :
            start = mid+1
    return -1

d = [1,4,9,16,25,32,46,78,99,101]

print(binary_search(d,9))
print(binary_search(d,100))
print(binary_search(d,78))
