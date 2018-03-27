# 來辦場Party吧! 輸入十個整數、存入一個名為people清單中 (表示我們的宴客人數)；之後會有五次詢問，每次會輸入清單開始和結束的位置，再輸出從開始到結束位置的總和。
import random

people = []
for i in range(0, 10):
    i = random.randint(1, 10)
    people.append(i)
print(people, end='\n')

for q in range(0, 5):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    while a == b:
        b = random.randint(1, 10)
    if a > b:
        a, b = b, a
    print('a = ', a, ', b = ', b, ', sum = ', sum(people[a-1:b]))
