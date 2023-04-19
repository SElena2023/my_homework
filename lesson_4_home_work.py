
#Завдання 1. Сума списку
import random
spusok=[]
index=0
suma_spusok=0

while len(spusok)<20:            #створюємо список з випадкових чисел
    elem=random.randint(1,50)
    spusok.append(elem)
    
for elem in spusok:         #рахуємо суму циклом for
    suma_spusok+=elem
    elem+=1
    
while index<len(spusok):    #рахуємо суму циклом while 
    suma_spusok+=spusok[index]
    index+=1
print(suma_spusok)
print(spusok)


#Завдання 2. Програма, яка виводить сама себе
with open(__file__, 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line)


#Завдання 3. Програма, що виводить сама себе задом наперед
with open(__file__, 'r') as file:
    lines = file.readlines()
    for line in reversed(lines):
        print(line.strip()[::-1])


# Завдання 4. Сума максимально можливими купюрами
bills = int(input())

def money(bills):
    denominations = [500, 200, 100, 50, 20, 10]
    giving = []
    for denom in denominations:
        while bills >= denom:
            giving.append(denom)
            bills -= denom
    return giving


giving = money(bills)
print(f"Видано {bills} грн. у вигляді:")
for giv in giving:
    print(f"{giv} грн. купюра")


# Завдання 5. Сума дрібними купюрами
bills = int(input())

def money(bills):
    denominations = [500, 200, 100, 50, 20, 10]
    giving = []
    for denom in reversed(denominations):
        max_giving = min(bills // denom, 10)
        for i in range(max_giving):
            giving.append(denom)
            bills -= denom
    return giving

giving = money(bills)
print(f"Видано {bills} грн. у вигляді:")
for giv in giving:
    print(f"{giv} грн. купюра")
