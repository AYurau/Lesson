class Vegetable:
    states = ["Отсутствует", "Цветение", "Зеленый", "Красный"]

    def __init__(self, index):
        self._index = index
        self._state = self.states[0]

    def grow(self):
        if self._state != self.states[-1]:
            current_state_index = self.states.index(self._state)
            self._state = self.states[current_state_index + 1]

    def is_ripe(self):
        return self._state == self.states[-1]


class Tomato(Vegetable):
    def __init__(self, index, variety):
        super().__init__(index)
        self.variety = variety

    def give_variety(self):
        return self.variety


class TomatoBush:
    varieties = ["Агата", "ДеБарао", "Бычье сердце", "Сливка"]

    def __init__(self, tomato_count):
        self.tomatoes = [Tomato(index, self.varieties[0]) for index in range(tomato_count)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Урожай собран')
        else:
            print("Не все помидоры созрели.")
            return False

    @staticmethod
    def knowledge_base():
        print("Harvest time for tomatoes should ideally occur\n"
              "when the fruit is a mature green and\n"
              "then allowed to ripen off the vine.\n"
              "This prevents splitting or bruising\n"
              "and allows for a measure of control over the ripening process.")


# Тесты
tomato_bush = TomatoBush(3)  # Инициализируем куст
gardener = Gardener("Иван", tomato_bush)  # Инициализируем садовника
gardener.knowledge_base()  # Выводим справку по садоводству

for tomato in tomato_bush.tomatoes:
    print(Tomato.give_variety(tomato))  # Сорт помидоров
while gardener.harvest() is False:
    gardener.work()  # Работаем пока помидоры не созреют
