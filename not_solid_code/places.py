from abc import ABC, abstractmethod


class Place(ABC):
    name: str

    @abstractmethod
    def get_monsters(self):
        pass


class Kostroma(Place):
    name = 'Kostroma'

    def get_monsters(self):
        print('Orcs hid in the forest')


class Tokyo(Place):
    name = 'Tokyo'

    def get_monsters(self):
        print('Godzilla stands near a skyscraper')
