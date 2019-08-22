# 안녕하세요, 매일프로그래밍 이번주 문제입니다.
 
# 주어진 정수가 4의 거듭제곱인지 확인하시오.

# Given an integer, check if it is a power of 4.



innum = input("Input Number : ")

def check_exp(num) :
	if num == 1 :
		print "1 is True for 4 in 0"
		return
	else :
		value = num / 4
		rest = num % 4

		while value >= 0 :
			if rest != 0 :
				print "False : %d is not for 4."%num
				break
			else :
				if value == 1 :
					print "True : %d is for 4."%num
					break
				else : 
					rest = value % 4
					value = value / 4

check_exp(innum)


# 이 코드를 더 줄일 수 있을까?
# False / True 말고 지수가 몇인지까지 알려주는 코드를 짜보자
