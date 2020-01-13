'''
*args : 여러개의 인자를 함수로 받고자 할 때. 즉 몇 개의 인자가 들어올지 모르는
상황에서 쓴다.

**kwargs : keyword argument의 줄임말. 특정 키워드가 입력되었을 때 다른 반응

'''

def lastName_FirstName(*Names):
    for name in Names:
        print("%s %s "% (name[0],name[1:3]), end=' ')
    print("\n")



lastName_FirstName('김연아')
lastName_FirstName('김연아','박지성')
lastName_FirstName('김연아','박지성','손흥민')



def introduceName(*args, **kwargs):
    for key,value in kwargs.items():
        if '김연아' in value:
            print("{} 는 축구선수가 아닙니다.".format(value))
        else:
            print("{} 은 축구선수입니다.".format(value))


introduceName(name1="김연아",name2="박지성",name3="손흥민")
