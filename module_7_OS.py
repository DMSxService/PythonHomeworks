import os, time

directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.abspath(file)
        try:
            filetime = os.path.getmtime(file)
        except:
            print('Не удаётся извлечь время создания файла')
            continue
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(directory)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения:'
              f' {formatted_time}, Родительская директория: {parent_dir}')
