maze = {
        'a':['e'],
        'b':['c','f'],
        'c':['b','d'],
        'd':['c'],
        'e':['a','i'],
        'f':['g','j'],
        'g':['h','f'],
        'h':['g','l'],
        'i':['e','m'],
        'j':['f','k','n'],
        'k':['j','o'],
        'l':['h','p'],
        'm':['i','n'],
        'n':['j','m'],
        'o':['k'],
        'p':['l']
        }

def my_maze(m,s,e):
    qu = []
    done = set()

    qu.append(s)
    done.add(s)

    while qu:
        temp = qu.pop(0)
        for x in m[temp]:
            if x not in done:
                done.add(x)
            if x in done and x != e:
                done.pop()
                
        
    
