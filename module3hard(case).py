import builtins
data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]
counter = 0
def calculate_structure_sum (data_structure):
    global counter
    if len(data_structure) != 0:
        elem = data_structure.pop(0)
        el_tp = type(elem)
        match el_tp:
            case builtins.list:
                data_structure.extend(elem)
            case builtins.str:
                data_structure.append(len(elem))
            case builtins.int:
                counter += elem
            case builtins.float:
                counter += elem
            case builtins.dict:
                data_structure.extend(elem.keys())
                data_structure.extend(elem.values())
            case builtins.bool:
                counter += int(elem)
            case builtins.tuple:
                data_structure.extend(elem)
            case builtins.set:
                data_structure.extend(elem)
        calculate_structure_sum(data_structure)
    return counter

result = calculate_structure_sum (data_structure)
print(result)
