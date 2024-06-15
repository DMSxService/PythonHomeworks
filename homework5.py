immutable_var = ("задача", 5.5, 11, "решение", False)
print(immutable_var)
mutable_list = ["задача", 5.5, 11, "решение", False]
print(mutable_list)
#immutable_var [1] = 6.6 #Нельзя выполнить эту операцию так как переменная не изменного типа и является кортежем.
mutable_list [1] = 6.6
mutable_list.append("добавка")
print(mutable_list)