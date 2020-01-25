
connection = {
                1 : [2,3],
                2 : [4,5],
                3 : [],
                4 : [],
                5 : []
            }


def all_conn(c,n):
    qu = []
    done = set()

    qu.append(n)
    done.add(n)

    while qu:
        t = qu.pop(0)
        print(t)
        for x in c[t]:
            if x not in done:
                qu.append(x)
                done.add(x)

all_conn(connection, 1)
