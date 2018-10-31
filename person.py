# import car class here
from car import Car

class Person:
    def __init__(self, name, occupation):
        self._name = name
        self._occupation = occupation

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

    @property
    def occupation(self):
        return self._occupation
    @occupation.setter
    def occupation(self,occupation):
        self.occupation = occupation

    @classmethod
    def has_oldest_car(cls):
        dict_list = list(map(lambda car: vars(car),Car._all))
        sorted_list = sorted(dict_list, key = lambda r: r['_year'])
        return vars(sorted_list[0]['_owner'])

    @classmethod
    def drives_a(cls, car_name):
        dict_list = list(map(lambda car: vars(car),Car._all))
        filtered = list(filter(lambda car: car['_make'] == car_name, dict_list))
        return list(map(lambda p: vars(p['_owner']), filtered))

    def drives_same_make_as_me(self):
        person = vars((list(filter(lambda car : vars(car)['_owner'] == self, Car._all))).pop())
        person_car_name = person['_make']
        listt = Person.drives_a(person_car_name)
        listt.pop(listt.index(vars(self)))
        return listt
