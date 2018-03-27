# 請做出一支能猜數字的程式：每次讓使用者猜一個整數，若猜對就輸出Bingo；使用者最多可以猜3次。(提示: Bingo後可以使用break來離開迴圈)
import random
a = 0
b = 101
ans = random.randint(a+1, b-1)

for gchance in range(0, 5):
    print(a+1, '~', b-1)
    g = int(input('guess='))

    if gchance != 4:
        if ans == g:
            print('BINGO!!')
            print('YOU GUESS', gchance+1, 'TIME!!')
            break
        elif ans > g:
            print('WRONG!!')
            a = g
        elif ans < g:
            print('WRONG!!')
            b = g
    else:
        print('NO CHANCE!!')
        print('ans=', ans)