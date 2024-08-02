import time


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        self.user = [self.nickname, self.password, self.age]


class Video:
    # video = None

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        self.video = [self.title, self.duration, self.time_now, self.adult_mode]

    def __str__(self):
        return self.video


class UrTube:
    users = []
    videos = []
    current_user = None
    video_names = []

    def log_in(self, nickname, password):
        if nickname in self.users:
            print(f'Мегаюзер')
        else:
            print(f'Гигаюзер')

    def register(self, nickname, password, age):
        us = User(nickname, password, age)
        print(f'In def register {us}')

    def log_out(self, current_user):
        pass

    def add(self, *roll):
        for i in roll:
            kin = Video.__str__(i)
            if i not in self.videos:
                self.videos.append(kin)
                self.video_names.append(kin[0])

    def get_videos(self, search):
        names_list = []
        for i in range(0, len(self.video_names)):
            if search.lower() in str(self.video_names[i]).lower():
                names_list.append(self.video_names[i])
        return names_list

    def watch_video(self, other):
        pass


# if __name__ == '__main__':
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
print(f'ur.current_user {ur.current_user}')
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
