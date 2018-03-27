# 一年一度的世界歌王大賽來啦！身為評審的你，請輸入五個歌手的名字與成績。接下來會有五次查詢的機會，每次查詢都可以讓觀眾輸入一個名字、來查看心愛的歌手。
# 如果歌手不在名單中，請輸出’這個人沒參賽喲’；如果歌手在名單中，請輸出該歌手的名字與成績
singer = {}
stay = 1
while stay == 1:
    print('1. input', end='\n')
    print('2. search', end='\n')
    print('3. show', end='\n')
    print('else. exit', end='\n')
    option = int(input('option = '))
    print(end='\n')

    if option == 1:
        name = input('name = ')
        grade = int(input('grade = '))
        singer[name] = grade
        print('===========')
        print(end='\n')
    elif option == 2:
        query = input('query name = ')
        print(singer.get(query, 'NO guy'))
        print('===========')
        print(end='\n')
    elif option == 3:
        print(singer)
        print('===========')
        print(end='\n')
    else:
        stay = 0