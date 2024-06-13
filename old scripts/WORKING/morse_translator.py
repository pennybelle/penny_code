import os
import time

# default data collection
char = 0
code = 0
space = " "
poof = ""

# english/digits
decoded = [
    "A",  # 0
    "B",  # 1
    "C",  # 2
    "D",  # 3
    "E",  # 4
    "F",  # 5
    "G",  # 6
    "H",  # 7
    "I",  # 8
    "J",  # 9
    "K",  # 10
    "L",  # 11
    "M",  # 12
    "N",  # 13
    "O",  # 14
    "P",  # 15
    "Q",  # 16
    "R",  # 17
    "S",  # 18
    "T",  # 19
    "U",  # 20
    "V",  # 21
    "W",  # 22
    "X",  # 23
    "Y",  # 24
    "Z",  # 25
    "0",  # 26
    "1",  # 27
    "2",  # 28
    "3",  # 29
    "4",  # 30
    "5",  # 31
    "6",  # 32
    "7",  # 33
    "8",  # 34
    "9"   # 35
]

# special characters
special = [
    "/",
    "\\"
]

# characters that will be removed
trash = [
    "'",
    ".",
    ",",
    "-",
]

# morse
encoded = [
    ".-",     # A
    "-...",   # B
    "-.-.",   # C
    "-..",    # D
    ".",      # E
    "..-.",   # F
    "--.",    # G
    "....",   # H
    "..",     # I
    ".---",   # J
    "-.-",    # K
    ".-..",   # L
    "--",     # M
    "-.",     # N
    "---",    # O
    ".--.",   # P
    "--.-",   # Q
    ".-.",    # R
    "...",    # S
    "-",      # T
    "..-",    # U
    "...-",   # V
    ".--",    # W
    "-..-",   # X
    "-.--",   # Y
    "--..",   # Z
    "-----",  # 0
    ".----",  # 1
    "..---",  # 2
    "...--",  # 3
    "....-",  # 4
    ".....",  # 5
    "-....",  # 6
    "--...",  # 7
    "---..",  # 8
    "----."   # 9
]

# create or overwrite morse.txt
morse = open("morse.txt", "w")
morse.writelines("")
morse.close()

# get input, convert it to uppercase, get length of input and set that as the loop limit
IN = input("enter your input to be translated to morse: ").upper()
length = len(IN)

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
    # if input is a special character, it is passed as itself
    elif OUT in special:
        OUT = OUT + space
    # if input is a character that isn't accepted in morse, it gets removed (or...trashed...lol)
    elif OUT in trash:
        OUT = poof
    # if input char isn't in any valid list, it breaks the loop and throws an error
    else:
        print("ERROR!!! INVALID INPUT DETECTED!!!\n\nInvalid Input =", OUT)
        break
    # print result character by character each loop until the loop is filled aka char = length
    print(OUT, end="")
    # write result to morse.txt, also char by char
    open("morse.txt", "a").writelines(OUT)
    # close file (good practice <3)
    morse.close()
    # move to the next character in the input
    char += 1
# when the loop ends, output terminal prints original input, pauses for 15 secs, and then closes
print("\n", IN)
time.sleep(15)
