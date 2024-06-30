if len(str_number) > 1:
    return first * get_multiplied_digits(int(str_number[1:]))
else:
    return first