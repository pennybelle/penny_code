import random
import time
import os


def clear(): os.system('cls')


score = int(0)
tries = int(0)
while True:
    num = random.randint(1, 3)
    if input("whats the number?\n") != str(num):
        tries += 1
        print("wrong, it was " + str(num) + ". score/tries = " + str(score) + "/" + str(tries) + "\n")
    else:
        score += 1
        tries += 1
        print("wowie zowie you guessed right! score/tries = " + str(score) + "/" + str(tries) + "\n")
    time.sleep(1.5)
    clear()
    continue
