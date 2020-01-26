def solveMaze(g,start,end):
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        v = p[-1]
        print("p is : %s"%p)
        print("v id : %s"%v)
        if v == end:
            return p
        for x in g[v]:
            if x not in done:
                qu.append(p+x)
                done.add(x)
                print("qu >>>>> %s"%qu)
                print("done >>>> %s"%done)
    return "?"



maze = {
    'a':['e'],
    'b':['c','f'],
    'c':['b','d'],
    'd':['c'],
    'e':['a','i'],
    'f':['b','g','j'],
    'g':['f','h'],
    'h':['g','l'],
    'i':['e','m'],
    'j':['k','f','n'],
    'k':['j','o'],
    'l':['h','p'],
    'm':['i','n'],
    'n':['m','j'],
    'o':['k'],
    'p':['l']
    }

print(solveMaze(maze,'a','p'))
