first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = [len(list(zip(first, second))[i][0]) - len(list(zip(first, second))[i][1])
                for i in range(0, min(len(second), len(first)))
                if len(list(zip(first, second))[i][0]) - len(list(zip(first, second))[i][1])]
second_result = [len(first[i]) == len(second[i]) for i in range(0, min(len(second), len(first)))]

print(list(first_result))
print(list(second_result))
