class Tomato:
    states = {0:'Green',
              1:'Yellow',
              2:'Red'}
    index = 0

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self,index):
        self._index +=1
        self._state = Tomato.states[index]

    def is_ripe(self,index):
        if index == len(Tomato.states)-1:
            return 'Созрел'


class TomatoBush:
    def __init__(self,count):
        self.tomato_list = [Tomato(index) for index in range(0, count-1)]

    def grow_all(self):
        for tomato in self.tomato_list:
            tomato.grow(Tomato.index)

    def all_are_ripe(self):
        return all([tomato.is_ripe(Tomato.index) for tomato in self.tomato_list])

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

    @staticmethod
    def knowledge_base():
        print('Справка по садоводству будет в обновлённой версии. Сорян:(')


    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Tomate_one', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()











