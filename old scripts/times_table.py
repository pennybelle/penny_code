rng = 101
for i in range(1, rng):
    for j in range(1, rng):
        print('{0} time {1} is {2}'.format(j, i, i * j))
    print('-' * 20)
