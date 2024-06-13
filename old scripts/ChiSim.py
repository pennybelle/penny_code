from datetime import date
import time
import sys
import os
import random

os.system('mode 50,20')

def end():
    print()
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def flush():
    sys.stdout.flush()

class Cat():

    def meow_animation(anim_delay):
        Cat.meow()
        while True:
            print(r'''
      ,-.       _,---._ __  / \
     /  /    .-'       `./ /   \
    (  (   ,'            `/    /|
     \  `-"             \'\   / |
      `.              ,  \ \ /  |
       /`.          ,'-`----Y   |
      (            ;        |   '
      |  ,-.    ,-'         |  /
      |  | (   |        chi | /
      )  |  \  `.___________|/
       ''     '"
meow...
            ''')
            time.sleep(anim_delay)
            clear()
            flush()
            print(r'''
     ,-.        _,---._ __  / \
    |  |     .-'       `./ /   \
    |  |   ,'            `/    /|
     \  `-"             \'\   / |
      `.              ,  \ \ /  |
       /`.          ,'-`----Y   |
      (            ;        |   '
      |  ,-.    ,-'         |  /
      |  | (   |        chi | /
      )  |  \  `.___________|/
       ''     '"
meow...
            ''')
            time.sleep(anim_delay)
            clear()
            flush()
            print(r'''
   ,-.          _,---._ __  / \
   \  \      .-'       `./ /   \
    \  \   ,'            `/    /|
     \  `-"             \'\   / |
      `.              ,  \ \ /  |
       /`.          ,'-`----Y   |
      (            ;        |   '
      |  ,-.    ,-'         |  /
      |  | (   |        chi | /
      )  |  \  `.___________|/
       ''     '"
meow...
            ''')
            time.sleep(anim_delay)
            clear()
            flush()
            print(r'''
     ,-.        _,---._ __  / \
    |  |     .-'       `./ /   \
    |  |   ,'            `/    /|
     \  `-"             \'\   / |
      `.              ,  \ \ /  |
       /`.          ,'-`----Y   |
      (            ;        |   '
      |  ,-.    ,-'         |  /
      |  | (   |        chi | /
      )  |  \  `.___________|/
       ''     '"
meow...
            ''')
            time.sleep(anim_delay)
            clear()
            flush()

    def mood(modifier):
        mood = 0 + modifier
        if 9 <= mood <= 10:
            Cat.zoom()
            modifier -= random.randrange(5, 7)
        if 6 <= mood <= 8:
            if modifier > 5:
                modifier -= random.randrange(1, 5)
            else: modifier += random.randrange(1, 3)
            Cat.meow_animation(0.25)
        if 3 <= mood <= 5:
            Cat.hiss()
            if modifier > 3:
                modifier -= random.randrange(1, 2)
            else: modifier += random.randrange(3, 7)
        if 0 <= mood <= 2:
            Cat.zzzz()

    def meow():
        string = 'meow...'
        for char in string:
            print(char, end='')
            time.sleep(0.05)
            flush()

    def zoom():
        string = 'ZOOOOOM!!!'
        for char in string:
            print(char, end='')
            time.sleep(0.1)
            flush()
        end()

    def zzzz():
        string = 'zzzzzzzzz......'
        for char in string:
            print(char, end='')
            time.sleep(0.1)
            flush()
        end()

    def hiss():
        string = 'HISSSS!!!'
        for char in string:
            print(char, end='')
            time.sleep(0.1)
            flush()
        end()

    def __init__(self, name):
        self.name = name
        print(f'Hi my name is {name}')

Chi = Cat('Chi')
# this loop is just me messing with how im gonna make the program run, its WIP
while True:
    delay = random.randrange(5, 15)
    mood = random.randrange(1, 10)
    Cat.mood(1)
    time.sleep(delay)