'''
모두의 알고리즘 05ch

두 자연수 a와 b의 최대공약수를 구하는 알고리즘을 만들어 보세요
'''
a = int(input("a : "))
b = int(input("b : "))


def gcd(a,b) :
    i = min(a,b)
    while True :
        if a % i == 0 and b % i == 0 :
            return i
        i = i - 1


print(gcd(a,b))
        
