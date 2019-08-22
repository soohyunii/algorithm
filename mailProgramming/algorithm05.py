# 안녕하세요, 매일프로그래밍 이번주 문제입니다.
# 주어진 string 에 모든 단어를 거꾸로 하시오.

# 예제)
# Input: “abc 123 apple”
# Output: “cba 321 elppa”


instring = input("input string : ").split()
outlist = []
word = []
aa = 0

for i in range(0, len(instring), 1):
	word = list(instring[i])
	for j in range(len(word)-1, -1, -1):
		aa = word[j]
		outlist.append(aa)
		if j == 0 :
			outlist.append(' ')
print "output string : %s" %(''.join(outlist))

