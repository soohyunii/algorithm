
# 정수(int)가 주어지면, 팰린드롬(palindrome)인지 알아내시오. 팰린드롬이란, 앞에서부터 읽으나 뒤에서부터 읽으나 같은 단어를 말합니다. 단, 정수를 문자열로 바꾸면 안됩니다.

# 예제)
# Input: 12345
# Output: False

# Input: -101
# Output: False

# Input: 11111
# Output: True

# Input: 12421
# Output: True




inputint = int(input("input : "))
i = 1
inputlist = []
a = inputint
reverselist = []

while inputint > i :
	i = i * 10
	if inputint < i :
		break

if i > 1 :
	i = i / 10
else :
	i = 1

while i != 1 :
	inputlist.append(a // i)
	a = a % i
	i = i / 10
	if i == 1 :
		inputlist.append(a)
		break

reverselist = list(reversed(inputlist))

if i == 1 and inputlist == [] :
	if a < 0 :
		inputlist.append(1)
		
if reverselist == inputlist :
	print "Output : True"
else :
	print "Output : False"
	