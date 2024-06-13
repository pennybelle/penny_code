import time
def p(): time.sleep(1)


score = int(0)


print("welcome to the quiz")
playing = input("wanna play? (y/n)\n")
if playing != "y".lower():
    quit()
print("great, lets start")
time.sleep(1.5)
if input("what does cpu stand for\n") != "central processing unit".lower():
    print("nope\n")
    score -= 1
else:
    print("yooo gg\n")
    score += 1
time.sleep(1.5)
if input("how about gpu?\n") != "graphics processing unit".lower():
    print("sorry ur wrong :C")
    score -= 1
else:
    print("ayeeee nice")
    score += 1
time.sleep(1.5)
