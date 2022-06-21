class koala:
    def __init__(self, type):
        self.weight = 30
        self.age = 1
        self.name = 0
        self.schast = 5
        self.type = type


    def menu(self):
        a = int(input("Подскажите, сколько времени?\n"))
        if 9<=a<12:
            self.utro()
        elif 12<=a<15:
            self.obed()
        elif 15<=a<17:
            self.poldnik()
        elif 17<=a<21:
            self.uzhin()
        elif 21<=a<=24 or 0<=a<9:
            self.kalik()
        else:
            print("Введите существующее время!")

    def utro(self):
        print("""что делать будем?:
        1. На зарядку
        2. Позавтракать""")
        a = int(input("Введите цифру: "))

        if a == 1:
            print("Отлично позанимались!")
            self.weight -= 1
            self.age += 0.2
            self.info()
        elif a == 2:
            print("""Что на завтрак?:
            1. Без завтрака
            2. Смузи
            3. Чизбургер""")
            b = int(input("Введите цифру: "))
            if b == 1:
                print("Ну и ладно!")
                self.weight -= 2
                self.age += 0.2
                self.info()
            elif b == 2:
                print("На детоксе")
                self.weight += 1
                self.age += 0.2
                self.info()
            elif b == 3:
                print("Пара - па - па - пам!")
                self.weight += 1
                self.age += 0.2
                self.schast += 0.2
                self.info()
            else:
                print("Промахнулись по клавишам)")
        else:
            print("Промахнулись по клавишам)")

    def obed(self):
        print("""Уже обед? Чем займемся?:
        1. Погулять
        2. Пообедать""")
        a = int(input("Введите цифру: "))
        if a == 1:
            print("Хорошая прогулка!!")
            self.weight -= 1
            self.age += 0.2
            self.schast += 0.2
            self.info()
        elif a == 2:
            print("""Что на обед?:
            1. Без обеда
            2. Кепчук
            3. Супчик""")
            b = int(input("Введите цифру: "))
            if b == 1:
                print("Ну и ладно!")
                self.weight -= 2
                self.age += 0.2
                self.schast -= 0.2
                self.info()
            elif b == 2:
                print("Фее...")
                self.weight -= 1
                self.age += 0.2
                self.schast -=0.2
                self.info()
            elif b == 3:
                print("Горячее, то что нужно!")
                self.weight += 1
                self.age += 0.2
                self.schast += 0.2
                self.info()
            else:
                print("Промахнулись по клавишам)")

    def poldnik(self):
        print("""Уже половина дня прошла...:
        1. Перекусить
        2. Поиграть в картишки""")
        a = int(input("Введите цифру: "))

        if a == 1:
            print("Вот и перекусили!")
            self.weight += 1
            self.age += 0.2
            self.schast += 0.2
            self.info()

        elif a == 2:
            print("Вот тебе два туза, неудачник!")
            self.weight += 0
            self.age += 0.2
            self.schast += 0.7
            self.info()
        else:
            print("Промахнулись по клавишам)")

    def uzhin(self):
        print("""Вечереет, планов пока что нету..:
        1. На танцы
        2. Поужинать""")
        a = int(input("Введите цифру: "))
        if a == 1:
            print("Хорошая потусили!!")
            self.weight -= 1
            self.age += 0.2
            self.schast += 0.2
            self.info()
        elif a == 2:
            print("""Что на ужин?:
            1. Без ужина
            2. Котлетки
            3. На шаурму?""")
            b = int(input("Введите цифру: "))
            if b == 1:
                print("Ну и ладно!")
                self.weight -= 2
                self.age += 0.2
                self.schast -= 0.2
                self.info()
            elif b == 2:
                print("Как будто мама приготовила")
                self.weight += 1
                self.age += 0.2
                self.schast -=0.4
                self.info()
            elif b == 3:
                print("Снова обляпался, зато вкусно!")
                self.weight += 1
                self.age += 0.2
                self.info()
            else:
                print("Промахнулись по клавишам)")

    def kalik(self):
        print("""Что на ужин?:
        1. На кальян
        2. Поспать""")
        b = int(input("Введите цифру: "))
        if b == 1 and self.age > 3:
            print("Наконец-то накурился!")
            self.age += 0.5
            self.schast += 4
            self.info()
        elif b == 1 and self.age < 3:
            print("Вам еще не исполнилось 3 года!")
            self.schast -= 0.2
            self.info()
        elif b == 2:
            print("Наконец-то этот день закончился")
            self.age += 0.4
            self.schast += 2
            self.info()

    def info(self):
        print(f"Вес = {self.weight}")
        print(f"Возраст = {self.age}")
        print(f"Счастье =  {self.schast}")

while True:
    a = input("Введите Имя коалы: ")
    koala1 = koala(a)

    while True:
        koala1.menu()