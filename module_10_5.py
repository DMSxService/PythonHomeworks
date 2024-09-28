import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as strings:
        string = strings.readline()
        while len(string) > 0:
            all_data.append(string)
            string = strings.readline()


filenames = [f'D:\\PythonHomeworks\\Other_files\\file {number}.txt' for number in range(1, 5)]

# Линейный вызов
# time_start = datetime.now()
# for i in filenames:
#     read_info(i)
# time_end = datetime.now()
# time_res = time_end - time_start
# print(f'{time_res} линейный')

# Многопроцессный
if __name__ == '__main__':
    time_start = datetime.now()
    with multiprocessing.Pool(processes=len(filenames)) as pool:
        pool.map(read_info, filenames)
    time_end = datetime.now()
    time_res = time_end - time_start
    print(f'{time_res} многопроцессный')

# 0:00:09.376185 линейный
# 0:00:04.227996 многопроцессный
