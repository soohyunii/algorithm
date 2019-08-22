import random

# data = list(input("num and string list input : "))
# numlist = []

# for i in range(0, len(data), 1):
# 	num = int(filter(str.isdigit,data[i]))
# 	numlist.append(num) 
# print numlist


## declare function ##
def getNumber(strData) :
	numStr = ''
	for ch in strData :
		if ch.isdigit() :
			numStr += ch
	return int(numStr)

## declare var ##
data = []
i,k = 0,0

## main code ##
if __name__ == "__main__" :
	for i in range(0,10) :
		tmp = hex(random.randrange(0,100000))
		tmp = tmp[2:]
		data.append(tmp)
	print "before data : %s"%data

	for i in range(0, len(data)-1) :
		for k in range(i+1, len(data)) :
			if getNumber(data[i]) > getNumber(data[k]) :
				tmp = data[i]
				data[i] = data[k]
				data[k] = tmp
	print 'after data : %s'%data


