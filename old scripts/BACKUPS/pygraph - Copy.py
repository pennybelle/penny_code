
adjustment = input("adjustment?\n")
y = int(1)
while True:
    x = int(y + 1)
    print("NEW VALUE - " + str(int(x)))
    while x != 1:
        if int(x % 2) == 0:
            x /= int(2)
            print("." * int(x / int(adjustment)))
            continue
        elif int(x % 2) != 0:
            x = int(3 * x + 1)
            print("." * int(x / int(adjustment)))
            continue
    while x == 1:
        print("-----------\nGAME OVER\n-----------")
        break
    y += int(1)
    continue
