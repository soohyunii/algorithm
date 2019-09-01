'''
모두의 알고리즘 05ch - 유클리드 알고리즘 사용하기

유클리드 알고리즘을 사용해 두 자연수 a와 b의 최대공약수를 구하는 알고리즘을 만들어 보세요

gcd(a,b)=gcd(b,a%b), gcd(n,0) = n

'''

a = int(input("a : "))
b = int(input("b : "))

def uc_gcd(a,b) :
    if b == 0 :
        return a
    return uc_gcd(b,a%b)
    

print(uc_gcd(a,b))
