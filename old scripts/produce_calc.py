import math
import time
log = open('produce_prices.log', 'w+')
log.close()

def equation(time, count, size, quantity=1, inflation=.3):
    output = ((time * size) / (count * quantity)) * inflation
    return math.ceil(output)

def pepper():
    return equation(time=172, count=2, size=2)
def tomato():
    return equation(time=172, count=2, size=1)
def zucc():
    return equation(time=172, count=2, size=3)
def pumpkin():
    return equation(time=259, count=2, size=4)
def potato():
    return equation(time=259, count=2, size=2)
def carrot():
    return equation(time=144, count=3, size=2)
def onion():
    return equation(time=288, count=2, size=2)
def garlic():
    return equation(time=700, count=4, size=1)
def kohlrabi():
    return equation(time=129, count=2, size=2)
def turnip():
    return equation(time=175, count=3, size=2)
def beetroot():
    return equation(time=175, count=2, size=2)
def radish():
    return equation(time=60, count=4, size=2)
def parsnip():
    return equation(time=288, count=3, size=2)
def sugarmelon():
    return equation(time=187, count=1, size=4)
def strawberry():
    return equation(time=80, count=6, size=1)
def wheat():
    return equation(time=345, count=5, size=2, quantity=10)
def pineapple():
    return equation(time=360, count=1, size=4)
def beans():
    return equation(time=273, count=2, size=1, quantity=20)

log = open('produce_prices.log', 'a')
log.writelines([f'''
pepper = {pepper()}
tomato = {tomato()}
zucc = {zucc()}
pumpkin = {pumpkin()}
potato = {potato()}
carrot = {carrot()}
onion = {onion()}
garlic = {garlic()}
kohlrabi = {kohlrabi()}
turnip = {turnip()}
beetroot = {beetroot()}
radish = {radish()}
parsnip = {parsnip()}
sugarmelon = {sugarmelon()}
strawberry = {strawberry()}
wheat = {wheat()}
pineapple = {pineapple()}
beans = {beans()}
'''])
log.close()

print('check produce_prices.log')
time.sleep(10)

# TODO - add functions to list and use for loop to cycle through each item