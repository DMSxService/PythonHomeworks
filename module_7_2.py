def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='UTF-8')
    strings_position = {}
    for i in range(0, len(strings)):
        strings_position[(i + 1, file.tell())] = strings[i]
        file.write(str(strings[i]) + '\n')
    file.close()
    return strings_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
