'''
연결되어 있는 모든 친구들의 리스트를 뽑고 친밀도를 계산합니다.
'''

connection = {
                "Summer":["John","Julia","Mike"],
                "John":["Summer","Julia"],
                "Julia":["John","Summer","Mike","Maria"],
                "Mike":["Summer","Julia"],
                "Maria":["Julia","Kevin"],
                "Kevin":["Maria"],
                "Tom":["Jerry"],
                "Jerry":["Tom"]
                }


def find_all_connection(con, name):
    
    qu = []
    done = set()

    qu.append((name,0))
    done.add(name)

    while qu:
        (x,y) = qu.pop(0)
        print(x,y)
        for friend_name in con[x]:
            if friend_name not in done :
                qu.append((friend_name,y+1))
                done.add(friend_name)


name = input("이름을 입력하세요 : ")
find_all_connection(connection,name)
