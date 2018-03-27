# 讓使用者在名為table的dict中，輸入五組的key-value pair，key是字串、value是數字，最後把這個dict印出來。(提示: dict沒有append，直接用增加或更新(InsertOrUpdate)的方式)
table = {}

for i in range(0, 5):
    k = input('key = ')
    v = int(input('value = '))
    table[k] = v
    print(end='\n')
print(table)