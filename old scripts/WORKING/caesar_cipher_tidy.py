import time
import random
import os

# default data collection
cipher = 'cipher.log'
key = []
OTP = []
OTP_request = ''
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# create or overwrite output.txt
file = open(cipher, 'w')
file.writelines('')
file.close()

# ask for input
word = input('input: ').upper()  # convert input to uppercase

# ask if this encryption will have a One-Time-Pad included, applying a shift key to the original key
while OTP_request != 'y' or 'n':
    OTP_request = input('one time pad(y/n): ').lower()
    if OTP_request == 'y':
        OTP_request = True
        break
    elif OTP_request == 'n':
        OTP_request = False
        break
    else:
        print('\nInvalid Input!\n')

for output in word:
    dice = random.randint(1, 26)  # roll the dice, gives back a pseudo-random number
    shift = random.randint(1, 73)  # shift that generates the one time key, and applies to the original key

    # check which letter = output, then applies the cipher
    if output in alp:
        output = alp.index(output) + dice  # converts str to index pos and adds shift from dice roll
        output = alp[output % 26]  # converts output back to str from new pos taken from previous line (mod 26)
    # if output isn't in the alp list it'll pass as itself, unencoded
    else:
        output = output
    # if user wants an OTP code, this applies the code shift to the original key
    if OTP_request:
        dice += shift  # add shift
    # this prevents characters that aren't letters from being keyed
    if output in alp:
        key.append(abs(dice))  # add the newest key list to key list (this gets printed after the loop finishes)
        if OTP_request:
            OTP.append(abs(shift))
    print(output, end='')
    file = open(cipher, 'a')
    file.writelines(output)
file.write(f'\n{key}')
print('\n' + str(key))
if OTP_request:
    file.write(f'\n{key}')
    print(OTP)
file.close()
print('check cipher.log')
time.sleep(300)
