import os
import time

# default data collection
char = 0
code = 0
space = ' '
file = 'morse.log'

# english/digits
decoded = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,?\'!/()&:;=+-_"$@|'

# morse
encoded = [
    '.-',       # A
    '-...',     # B
    '-.-.',     # C
    '-..',      # D
    '.',        # E
    '..-.',     # F
    '--.',      # G
    '....',     # H
    '..',       # I
    '.---',     # J
    '-.-',      # K
    '.-..',     # L
    '--',       # M
    '-.',       # N
    '---',      # O
    '.--.',     # P
    '--.-',     # Q
    '.-.',      # R
    '...',      # S
    '-',        # T
    '..-',      # U
    '...-',     # V
    '.--',      # W
    '-..-',     # X
    '-.--',     # Y
    '--..',     # Z
    '-----',    # 0
    '.----',    # 1
    '..---',    # 2
    '...--',    # 3
    '....-',    # 4
    '.....',    # 5
    '-....',    # 6
    '--...',    # 7
    '---..',    # 8
    '----.',    # 9
    '.-.-.-',   # .
    '--..--',   # ,
    '..--..',   # ?
    '.----.',   # '
    '-.-.--',   # !
    '-..-.',    # /
    '-.--.',    # (
    '-.--.-',   # )
    '.-...',    # &
    '---...',   # :
    '-.-.-.',   # ;
    '-...-',    # =
    '.-.-.',    # +
    '-....-',   # -
    '..--.-',   # _
    '.-..-.',   # "
    '...-..-',  # $
    '.--.-.',   # @
    '..-.-',    # ¿
    '--...-',   # ¡
    '.-.-.',    # | aka full stop
]

# create or overwrite morse.txt
morse = open(file, 'w')
morse.writelines('[ ')
morse.close()

# get input, convert it to uppercase, get length of input and set that as the loop limit
IN = input('input: ').upper()
length = len(IN)
print('[ ', end='')
# start the loop with step at 0, increasing by 1 until it reaches the length of the input
while char != length:
    # set output as input (character by character, moves to next char each loop)
    OUT = IN[char]
    # if input is a space, convert it to 3 spaces (value is 2 because each char already comes with a space)
    if OUT == space:
        OUT = space * 2
    # if input character is in the decoded list, it encodes the character
    elif OUT in decoded:
        code = decoded.index(OUT)
        OUT = encoded[code] + space
    # if input char isn't in any valid list, it breaks the loop and throws an error
    else:
        print('Invalid Input =', OUT[char], end=' ')
        break
    # print result character by character each loop until the loop is filled aka char = length
    print(OUT, end='')
    # write result to morse.log, writes characters one by one until fully decoded
    open(file, 'a').writelines(OUT)
    # move to the next character in the input
    char += 1
# when the loop ends, output terminal prints original input, pauses for 15 secs, and then closes
print(']')
open(file, 'a').writelines(']')
# close file (good practice <3)
morse.close()
time.sleep(300)
