
y = list[]

y.append(295147905179352825856)

while True:
    x = y
    print("NEW VALUE - " + str([x]))
    while x != 1:
        if int(x % 2) == 0:
            x /= int(2)
            print("DOWN - " + str([x]))
            continue
        elif int(x % 2) != 0:
            x = int(3 * x + 1)
            print("UP - " + str([x]))
            continue
    while x == 1:
        print("\n" * 100 + "-----------\nGAME OVER\n-----------" + "\n" * 100)
        break
    y.clear()
    y.append(y + 1)
    continue
