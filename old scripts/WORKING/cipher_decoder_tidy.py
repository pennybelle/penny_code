import os
import sys
import time

# default data collection
index = 0
OTP = []
OTP_check = ''
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    OTP_check = input('OTP? (y/n)\n').lower()
    if OTP_check == 'y':
        OTP_check = True
        break
    elif OTP_check == 'n':
        OTP_check = False
        break
    else:
        print('invalid input')

word = input('encoded msg: ')
key = input('key: ').strip('[]').split(', ')
if OTP_check:
    OTP = input('otp: ').strip('[]').split(', ')
log = open('cipher_decoded.log', 'w')
log.close()
log = open('cipher_decoded.log', 'a')

for word_char in word:
    if word_char in alp:
        key_char = key[index]
        key_char = int(key_char)
        if OTP_check:
            OTP_char = OTP[index]
            OTP_char = int(OTP_char)
            key_char = key_char - OTP_char
        word_char = alp.index(word_char) - key_char
        word_char = alp[word_char % 26]
        index += 1
    elif not alp:
        word_char = word_char
    log.write(word_char)
    print(word_char, end='')
    sys.stdout.flush()
log.close()
time.sleep(300)
