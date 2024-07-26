import time
class User:
    def __init__(self, nickname, password, age):
        self.nickname = ''
        self.password = ''
        self.age = int()

    def __str__(self):
        return str(self)

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    current_user = None
    def __init__(self):
        self.users = []
        self.videos = []

    def log_in(self, login, password):
        for usr in self.users:
            if login == str(usr) and hash(password) == hash(usr.password):
                self.current_user = usr
                break
            elif login == str(usr) and hash(password) != hash(usr.password):
                print('Не верный пароль')
                break
            else:
                print('Такого пользователя не существует')

    def register(self, nickname, password, age):
        user = User
        user.nickname = nickname
        user.password = password
        user.age = age
        if not self.users:
            self.users.append(user)
            self.current_user = user
        for u in self.users:
            if str(user) == str(u):
                print(f'Пользователь {nickname} уже существует')
                break
            else:
                self.users.append(user)
                self.current_user = user
                break

    def log_out(self):
        current_user = None

    def add(self, *args):
        for vid in args:
            vid_is_exist = False
            for v in self.videos:
                if vid.title == v.title:
                    print('Существует')
                    vid_is_exist = True
                    break
            if vid_is_exist:
                break
            else:
                self.videos.append(vid)

    def get_videos(self, word):
        search_list = []
        for vid in self.videos:
            str_lower = str(vid.title).lower()
            if word.lower() in str_lower:
                search_list.append(vid.title)
        if not search_list:
            print('Ничего не найдено')
        else:
            return search_list

    def watch_video(self, title_for_play):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for vid in self.videos:
                if vid.title == title_for_play:
                    if vid.adult_mode and self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        while vid.time_now < vid.duration:
                            print(vid.time_now + 1, end= ' ')
                            vid.time_now += 1
                            time.sleep(1)
                        print('Конец видео')



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