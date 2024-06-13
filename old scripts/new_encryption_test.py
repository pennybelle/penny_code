import random

class cipher():
    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def encoder(input=input('Input: ').upper):
        encoded = ''
        encoded_one = ''
        encoded_two = ''
        key_one = []
        key_two = []
        for char in input():
            if char in cipher.alp:
                print(f'char = {char}')
                shift_one = random.randrange(10, 74)
                print(f'1st shift - {shift_one}')
                shift_two = random.randrange(10, 74)
                print(f'2nd shift - {shift_two}')
                shift_temp = cipher.alp.index(char) - shift_one
                key_one.append(shift_one)
                encoded = cipher.alp[shift_temp % 26]
                print(f'encoded = {encoded}')
                encoded_one += encoded
                print(f'encoded one = {encoded_one}')
                shift_temp = cipher.alp.index(encoded) - shift_two
                key_two.append(shift_two)
                encoded = cipher.alp[shift_temp % 26]
                print(f'encoded = {encoded}')
                encoded_two += encoded
                print(f'encoded two = {encoded_two}')
        print(*key_one)
        print(*key_two)
        return cipher.alp.index(encoded_two)

print(cipher.encoder())