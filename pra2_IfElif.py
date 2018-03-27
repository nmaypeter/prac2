# 寫一支Python整數機，第一步讓使用者輸入想要做的符號運算，比如「+, -, *, /」，第二步讓使用者輸入’整數1’和 ‘整數2’，最後讓這兩個整數進行運算。如果輸入的運算符號不是「+, -, *, /」，便輸出「錯誤」。
o = input('operation=')
a = int(input('first int= '))
b = int(input('second int= '))

if o == '+':
    print(a, "+", b, "=", a + b)
elif o == '-':
    print(a, "-", b, "=", a - b)
elif o == '*':
    print(a, "*", b, "=", a * b)
elif o == '/':
    print(a, "/", b, "=", a / b)
else:
    print('ERROR')
