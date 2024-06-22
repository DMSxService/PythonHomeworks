number = int(input("Введите число от 3 до 20 : "))
pass_number =[]
str_pass_number = "Password: "
while number < 3 or number >20:
    print("Вы ввели не корректное число, попробуйте еще раз")
    number = int(input("Введите число от 3 до 20 : "))
for i in range(1,number) :
    for j in range(i,number) :
        if i == j :
            continue
        elif not(number%(i+j)) :
            str_pass_number = str_pass_number + str(i) + str (j)
print(str_pass_number)
