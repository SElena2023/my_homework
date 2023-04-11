#Практика

#Задача 1. Перевірити, чи є введене число парним
ch=int(input("Уведіть будь-яке число\n"))

if not ch:
    print("0 не є ні парним ні непарним")
elif (ch%2): 
    print("число непарне")
else:
    print("число парне")

# Задача 2. Перевірити, чи є число не парним,
#ділиться чи на три і на п'ять одночасно,
#але так, щоб не ділитися на 10
ch=int(input("Уведіть будь-яке число\n"))
if (ch%2 and not ch%3 and not ch%5 and ch%10):
    print(ch,"не парне, ділиться  на три і на п'ять одночасно, але  не ділитися на 10")


#Задача 3. Ввести число, вивести усі його дільники
print("Bивести усі дільники числа")
ch=int(input("Уведіть будь-яке число"))
for i in range(1,ch//2+1):
    if not(ch%i):
        print(i,sep=" ")
print(ch)

#Задача 4. Ввести число, вивести його розряди та їх множники
ch=int(input("Уведіть будь-яке число\n"))
roz=1
list=[]
while ch:
    ost=ch%10
    ch=ch//10
    list.append(str(ost)+"*10^"+str(roz))
    roz+=1
print("+".join(list[::-1]))

#Свій приклад. Виводимо числа від 1 до 100.
#якщо число кратне 3, виводимо Fizz
#якщо число кратне 5, виводимо Buzz
#якщо число кратне 3 і 5, виводимо FizzBuzz
for i in range(1, 101):
    print('FizzBuzz' if i%3==0 and i%5==0 else 'Fizz' if i%3==0 else 'Buzz' if i%5==0 else i) 
        

#Задача Fizz-Buzz
fizz = int(input("Enter fizz: "))
buzz = int(input("Enter buzz: "))
n = int(input("Enter n: "))

for i in range(1, n+1):
    output = ""
    if i % fizz == 0:
        output += "F"
    if i % buzz == 0:
        output += "B"
    if output == "":
        output = str(i)
    print(output) 
