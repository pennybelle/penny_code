import os
import sys
import time

# default data collection
morse = 0
check = 0
letter = 0
step = 0
decoded = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,?\'!/()&:;=+-_"$@'
default_encoded = [
    ".-",       # A
    "-...",     # B
    "-.-.",     # C
    "-..",      # D
    ".",        # E
    "..-.",     # F
    "--.",      # G
    "....",     # H
    "..",       # I
    ".---",     # J
    "-.-",      # K
    ".-..",     # L
    "--",       # M
    "-.",       # N
    "---",      # O
    ".--.",     # P
    "--.-",     # Q
    ".-.",      # R
    "...",      # S
    "-",        # T
    "..-",      # U
    "...-",     # V
    ".--",      # W
    "-..-",     # X
    "-.--",     # Y
    "--..",     # Z
    "-----",    # 0
    ".----",    # 1
    "..---",    # 2
    "...--",    # 3
    "....-",    # 4
    ".....",    # 5
    "-....",    # 6
    "--...",    # 7
    "---..",    # 8
    "----."     # 9
    ".-.-.-",   # .
    "--..--",   # ,
    "..--..",   # ?
    ".----.",   # '
    "-.-.--",   # !
    "-..-.",    # /
    "-.--.",    # (
    "-.--.-",   # )
    ".-...",    # &
    "---...",   # :
    "-.-.-.",   # ;
    "-...-",    # =
    ".-.-.",    # +
    "-....-",   # -
    "..--.-",   # _
    ".-..-.",   # "
    "...-..-",  # $
    ".--.-.",   # @
]

encoded = input('input: ').split(' ')
encoded = list(encoded)
length = len(encoded)

log = open('morse_decoded.log', 'w')
log.close()

log = open('morse_decoded.log', 'a')
print('output:', end='')
sys.stdout.flush()
while step < length:
    while encoded[morse] in default_encoded and encoded[morse] != default_encoded[check]:
        check += 1
    if encoded[morse] not in default_encoded:
        conversion = ' '
    else:
        conversion = decoded[check]
    print(conversion, end='')
    sys.stdout.flush()
    log.write(conversion)
    step += 1
    morse += 1
    check = 0
log.close()
time.sleep(300)
