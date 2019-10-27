'''
주어진 문장이 회문인지 아닌지 찾기(큐와 스택의 특징을 이용)
큐의 특징 - array.pop(0)
스택의 특징 - array.pop()

입력: 문자열 s
출력: 회문이면 True, 아니면 False
'''

def palindrome(s):
    qu = []
    st = []

    for x in s:
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())
    while qu:
        if qu.pop(0) != st.pop():
            return False
    return True

print(palindrome("Wow"))
print(palindrome("Madam, I'm adam."))
print(palindrome("Madam, I am Adam."))
            



