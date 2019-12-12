t = [1,3,5,7,9,11,13,23,57,109]

for i in enumerate(t):
    print(i)

'''
(0, 1)
(1, 3)
(2, 5)
(3, 7)
(4, 9)
(5, 11)
(6, 13)
(7, 23)
(8, 57)
(9, 109)
'''

for i,p in enumerate(t):
    print("index: {}, value: {}".format(i,p))


'''
index: 0, value: 1
index: 1, value: 3
index: 2, value: 5
index: 3, value: 7
index: 4, value: 9
index: 5, value: 11
index: 6, value: 13
index: 7, value: 23
index: 8, value: 57
index: 9, value: 109
'''
