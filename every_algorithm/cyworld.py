'''
191203 : 풀다가 중간에 끊김. 다시하자
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
    done = []

    while name in con:
        for friend_name in con[name]:
            qu.append(friend_name)
            
        
    if name not in con:
        print("해당하는 이름이 없습니다.")
        #find_all_connection(con)

name = input("이름을 입력하세요 : ")
print(find_all_connection(connection,name))
