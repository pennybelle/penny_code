todo = []

while True:
    cont = str(input('\n\n0 - Remove Item   |   1 - Add Item\n\n'))
    if str(1) in cont:
        cont = cont.strip('0')
        todo.append(cont)
    elif str(0) in cont:
        cont = cont.strip('1')
        todo.remove(todo.index(cont))
    if len(todo) > 0:
        for i in todo:
            print(todo.index(i), i)