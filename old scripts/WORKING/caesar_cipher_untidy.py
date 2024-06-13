import time
import random
import os

# default data collection
cipher = 'cipher.log'
step = 0
extra = 0
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
length = len(word)  # get length of input in total character sum
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

while step != length:  # each loop increases step by 1. once step is equal to the length of the input the loop breaks
    output = word[step]  # splits input into characters, proceeds to the next char each loop
    dice = random.randint(1, 26)  # roll the dice, gives back a pseudo-random number
    shift = random.randint(1, 73)  # shift that generates the one time key, and applies to the original key

    # check which letter = output, then applies the cipher
    if output in alp:
        output = alp.index(output) + dice
        output = alp[output % 26]
    # if output isn't in the alp list it'll pass as itself, unencoded
    elif output not in alp and extra != length:
        output = output
        extra += 1  # extra is just a failsafe to make sure the loop eventually stops
        continue
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
    step += 1
file.write('\n{}'.format(key))
if OTP_request:
    file.write('\n{}'.format(OTP))
file.close()
print('\n' + str(key))
if OTP_request:
    print(OTP)
else:
    print('')
print('check cipher.log')
time.sleep(300)
