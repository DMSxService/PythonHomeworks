first = input("Введите первое число ")
try:
    first = int(first)
except : print(first, " не является числом, программа будет завершена!"), exit()
second = input("Введите второе число ")
try:
    second = int(second)
except : print(second, " не является числом, программа будет завершена!"), exit()
third = input("Введите третье число ")
try:
    third = int(third)
except : print(third, " не является числом, программа будет завершена!"), exit()
if (first == second) and (second == third) :
    print(3)
elif (first == second) or (second == third) or (first == third) :
    print(2)
else:
    print(0)
