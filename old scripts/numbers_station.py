import random
import os
class cipher():
    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def clear(): os.system('cls' if os.name == 'nt' else 'clear')
    def encoder(msg):
        encoded = ''
        encoded_index = ''
        key_one = ''
        key_two = ''
        # convert each letter into a number and apply each shift individually
        for char in msg():
            if char in cipher.alp:
                shift_one = random.randrange(10, 74)
                shift_two = random.randrange(10, 74)
                encoded = cipher.alp.index(char) - shift_one
                key_one += str(shift_one) + ' '
                encoded = cipher.alp[encoded % 26]
                encoded = cipher.alp.index(encoded) - shift_two
                key_two += str(shift_two) + ' '
                encoded = cipher.alp[encoded % 26]
                encoded_index += str(f'{cipher.alp.index(encoded) + int(1):02} ')
            elif char == ' ':
                pass
            else:
                print(f'Error: Character \'{char}\' is not allowed in the input')
                break
        raw = input('Raw encryption? ')
        if raw == 'y' or raw == 'yes':
            output = f'{key_one}{key_two}{encoded_index}'
        else:
            output = f'''[ - garbled carnival music plays - ]
[ - female voice begins reading - ]\n
{key_one}{key_two}{encoded_index}\n
[ - garbled carnival music plays - ]'''
        print(output)
        import subprocess 
        subprocess.run('pbcopy', text=True, input=output)

        return

    def decoder(input):
        # mark the length of the message based on len of the input // 3
        length = len(input) // 3
        # split the list into 3 parts (the two keys and the message)
        key_one = input[:length]
        key_two = input[length:length * 2]
        encoded = input[length * 2:]
        # for each number in the length, apply the keys and output index of alp
        for index, key in enumerate(encoded):
            if len(encoded) == length:
                key = int(key) # convert key to int
                k_one = int(key_one[index])
                k_two = int(key_two[index])
                final_key = key + (k_one + k_two) - 1
                print(cipher.alp[final_key % 26], end='', flush=True)
            elif len(encoded) < length:
                print('Error: Message is longer than keys')
                break
            elif len(encoded) > length:
                print('Error: Message is shorter than keys')
                break
        print()
        return


while True:
    cipher_type = input('\nE - Encode\nD - Decode\n\n').upper()
    cipher.clear()
    if cipher_type == 'E':
        cipher.encoder(input('Plain Text: ').upper)
    elif cipher_type == 'D':
        cipher.decoder(list(input('Encryption: ').split(' ')))
    else:
        print('Invalid Input')