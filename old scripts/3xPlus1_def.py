def equation(x):
    x = int(x)
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        print(x)
        continue


equation(input('input: '))
