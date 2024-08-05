import time


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


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
    current_age = None
    video_names = []

    def log_in(self, nickname, password):

        for i in range(0, len(self.users)):
            us = self.users[i]
            if nickname == us[0] and hash(password) != us[1]:
                return
        self.current_user = nickname
        return 1

    def register(self, nickname, password, age):
        us = self.log_in(nickname, password)
        if us == 1:
            self.users.append([nickname, hash(password), age])
        else:
            print(f"Пользователь {nickname} уже существует")
        return

    def log_out(self, current_user):
        self.current_user = None

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

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for i in range(0, len(self.videos)):
            vs = self.videos[i]
            if title == vs[0]:
                if vs[3]:
                    for j in range(0, len(self.users)):
                        us = self.users[j]
                        if self.current_user == us[0] and us[2] < 18:
                            print("Вам нет 18 лет, пожалуйста покиньте страницу")
                            return
                for j in range(1, vs[1] + 1):
                    time.sleep(1)
                    print(j, end=" ")
                print('Конец видео')
                time.sleep(1)
                vs[1] = 0
        return
        #         self.current_user = nickname
        # self.current_user[2] < 18:
        # print("Вам нет 18 лет, пожалуйста покиньте страницу")


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
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
