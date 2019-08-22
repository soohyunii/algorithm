# 안녕하세요, 매일프로그래밍 이번주 문제입니다.
# 주어진 string 에 모든 단어를 거꾸로 하시오.

# 예제)
# Input: “abc 123 apple”
# Output: “cba 321 elppa”

instring = str(input("input string : "))
liststring = list(instring)
outlist = []
aa = 0

for i in range(len(liststring)-1, -1, -1):
	aa = liststring[i]
	outlist.append(aa)
print "output string : %s" %outlist

