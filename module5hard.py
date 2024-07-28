users = []
videos = []


class User:
    def __init__(self, nickname, password, age):
        users.append({nickname: [password, hash(password), age]})


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        videos.append({title: [duration, time_now, adult_mode]})


class UrTube:

    def __init__(self):
        pass

    def log_in(self):
        pass

    def register(self, nickname, password, age):
        pass

    def log_out(self, current_user):
        pass

    def add(self, *other):
        if not (self in videos):
            videos.append(self)
            print('No cinema')
        else:
            print('Cinema exist')

    def get_videos(self, search):
        if search in videos:
            print(search)
        elif search in videos:
            print(videos)
        elif search in videos:
            print(search)
        else:
            print(f' {videos}Cinema not found')

    def watch_video(self, other):
        pass


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
