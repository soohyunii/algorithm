from fractions import Fraction

innum = int(input())

def fraction_sum(innum) :

    arraysum = 0
    lastnum = 0
    result = []

    for i in range(1, 10000001, 1) :
        arraysum += i
        if innum > arraysum :
            continue
        elif innum == arraysum :
            if i%2 == 0 :
                result.append(1)
                result.append(i)
                print ("%s/%s"%(result[0],result[1]))
                break
            else :
                result.append(i)
                result.append(1)
                print ("%s/%s"%(result[0],result[1]))
                break
        else :
            lastnum = i-((arraysum-innum)+1)
            if i%2 == 0 :
                result.append(1+lastnum)
                result.append(i-lastnum)
                print ("%s/%s"%(result[0],result[1]))
                break
            else :
                result.append(i-lastnum)
                result.append(1+lastnum)
                print ("%s/%s"%(result[0],result[1]))
                break

fraction_sum(innum)


