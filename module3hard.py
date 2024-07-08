data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]
counter = 0
def calculate_structure_sum (data_structure):
    global counter
    if len(data_structure) != 0:
        elem = data_structure.pop(0)
        if isinstance(elem, list):
            data_structure.extend(elem)
        elif isinstance(elem, str):
            data_structure.append(len(elem))
        elif isinstance(elem, int):
            counter += elem
        elif isinstance(elem, float):
            counter += elem
        elif isinstance(elem, dict):
            data_structure.extend(elem.keys())
            data_structure.extend(elem.values())
        elif isinstance(elem, bool):
            counter += int(elem)
        elif isinstance(elem, tuple):
            data_structure.extend(elem)
        elif isinstance(elem, set):
            data_structure.extend(elem)
        calculate_structure_sum(data_structure)
    return counter

result = calculate_structure_sum (data_structure)
print(result)
