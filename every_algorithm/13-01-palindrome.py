'''
큐와 스택을 이용하지 않고 회문인지 아닌지 판단하는 방법이 있습니다.
문장의 앞뒤를 차례대로 비교하면서 각 문자가 같은지 확인하는 방법입니다.
이 방법으로 회문인지 아닌지 판단하는 알고리즘을 만들어보세요.
'''

def palindrome_nogada(str):
    i = len(str)-1
    j = 0
    while i>0:
        if str[j].isalpha()!=True:
            j += 1
        elif str[i].isalpha()!=True:
            i -= 1
        elif j.isalpha() and str[i].isalpha():
            print("j == %s"%j)
            print("str[i] == %s"%str[i])
            if str[i].lower() != j.lower():
                return False
            else:
                i -= 1
                j += 1
        else:
            i -= 1
            j += 1
    return True


#print(palindrome_nogada("Wow"))
print(palindrome_nogada("Madam,I'm Adam."))
#print(palindrome_nogada("Apple"))
