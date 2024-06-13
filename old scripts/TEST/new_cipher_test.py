import random
import sys
class Cipher():
    alp = 'abcdefghijklmnnopqrstuvwxyz'
    key = []
    def get_input():
        inpt = input('Input: ')
        key = list(input('Key: ').split('0'))
        return inpt, key

    def encode(inpt):
        for char in inpt:
            shift = []
            shift.append(random.randrange(1, 10))
            print(shift)
            for shift_num in shift:
                shift_num += int(shift[shift_num % 10])
                print(shift_num)
            Cipher.key.append(shift)
            char = Cipher.alp.index(char) + shift
            char = Cipher.alp[shift % 26]
            print(char, end='')
            sys.stdout.flush()
        output = str(Cipher.key).strip('[]').replace(',', '').replace(' ', '0')
        print('\n' + output)

# Cipher.get_input()
Cipher.encode(input('type something: '))