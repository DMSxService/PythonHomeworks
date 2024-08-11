def add_everything_up(a, b):
    try:  # if type(a) != int or type(b) != int or type(a) != float or type(b) != float:
        a + b
    except TypeError:
        return str(a) + str(b)
    return "{:.3f}".format(a+b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
