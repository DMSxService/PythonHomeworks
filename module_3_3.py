def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params()                                              # Вывод в консоль :    1 строка True
print_params(10)                                            # Вывод в консоль :    10 строка True
print_params('Проверочный текст', 12)                  # Вывод в консоль :    Проверочный текст 12 True
print_params(b = 25)                                        # Вывод в консоль :    1 25 True
print_params(c = [1,2,3])                                   # Вывод в консоль :    1 строка [1, 2, 3]
values_list = [7,12.3,False]
values_dict = {'a': 17, 'b': 'предложение','c': False}
print_params(*values_list)                                  # Вывод в консоль :    7 12.3 False
print_params(**values_dict)                                 # Вывод в консоль :    17 предложение False
values_list_2 = [23.3,71]
print_params(*values_list_2,'Истина')                     # Вывод в консоль :    23.3 71 Истина