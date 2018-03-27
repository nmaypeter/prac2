# 請輸出一個九九乘法表。(提示1: for loop裡面也可以有第二個for loop噢!)
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end=' ')
    print(end='\n')