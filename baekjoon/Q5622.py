instring = list(input())

alphalist = [['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],
             ['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
numberlist = []
timesum = 0

for k in range(0, len(instring), 1) :
    for i in range(0, len(alphalist), 1) :
        for j in range(0, len(alphalist[i]), 1) :
            if instring[k] in alphalist[i][j] :
                numberlist.append(i+2)
                timesum += i+3
print (timesum)

        
        
        
