# 現在有一個 list a = [1, 3, 5, 7, 9]，請對每一個元素都平方後印出來，且須將 a 也變成 [1, 9, 25, 49, 81]。
a = [1, 3, 5, 7, 9]
for i in range(0, len(a)):
    a[i] = a[i] ** 2
    print(a[i])
print(a)