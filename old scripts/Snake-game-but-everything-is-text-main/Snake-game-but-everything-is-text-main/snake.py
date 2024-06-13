import os
import random
a_counter = 0
b_counter = 0
lol = 0
right = True
left = False
up = False
hit = False
balance = False
a_x = random.randint(0,29)
a_y = random.randint(0,29)
first = False
down = False
end = False
import time,keyboard
counter = 0
length = 3
x = 0
y = 0
parts = []
scene = ("*"*30 + "\n")*30
ax_choice = []
ay_choice = []
dont_put_apples_here = []
for num in range(0,29):
    ax_choice.append(num)
    ay_choice.append(num)

eat = False
while not end:
    for num in range(0,29):
        ax_choice.append(num)
        ay_choice.append(num)

    if keyboard.is_pressed('d') and not left:
        right = True
        left,up,down = False,False,False
    elif keyboard.is_pressed('a') and not right:
        left = True
        up,down,right = False,False,False
    elif keyboard.is_pressed('w') and not down:
        up = True
        down,right,left = False,False,False
    elif keyboard.is_pressed('s') and not up:
        down = True
        up,right,left = False,False,False
    if right:
        x += 1
        
    elif left:
        x -= 1
        
    elif up:
        y -= 1
        
    elif down:
        y += 1
        
    if x % 30 == 0 and x != 0:
        x -= 1
        end = True
    if y == 30:
        y -=1
        end = True
    if y == -1:
        y +=1
        end = True
    if x == -1:
        x +=1
        end = True

    counter += 1
    scene = list(scene)
    parts.append(x+(y*31))
    scene[x+(y*31)] = "S"
    if counter == length :
        scene[parts[0]] = "*"
        del parts[0]
        counter -= 1
    for indices in parts:
        for ind in parts:
            if indices == ind and not a_counter == b_counter:
                end = True
            b_counter += 1
            
        b_counter = 0
        a_counter += 1
    a_counter = 0
    
    


    time.sleep(0.1)
    
    scene = list(scene)
    if a_x == x and a_y == y:
        eat = True
    if not eat:
        scene[a_x+(a_y*31)] = "a"
    dump = ""
    for ch in scene:
        dump += ch
    os.system('cls')
    print(dump)

    if eat:
        for indices in parts:
            i_x = indices%31
            i_y = (indices-i_x)/31

            ax_choice.remove(i_x)

            ay_choice.remove(int(i_y))
            


        length += 1
        a_x = random.choice(ax_choice)
        a_y = random.choice(ay_choice)
    
    
    eat = False
print('You died lol')