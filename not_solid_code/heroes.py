from abc import ABC, abstractmethod

from antagonistfinder import AntagonistFinder


class Media:

    def create_news(self, place):
        place_name = getattr(place, 'name', 'place')
        print(f'{self.name} saved the {place_name}!')


class Attack(ABC):

    @abstractmethod
    def attack(self):
        pass


class FireGun(Attack):

    def attack(self):
        print('PIU PIU')


class RoundhouseKick(Attack):

    def attack(self):
        print('Bump')


class Kick(Attack):

    def attack(self):
        print('Kick')


class Ultimate:

    def ultimate(self):
        print('Wzzzuuuup!')


class AbstractHero(ABC):

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)


class SuperHero(AbstractHero):
    pass


class Superman(SuperHero, Media, Kick, Ultimate):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)


class ChuckNorris(SuperHero, Media, FireGun):

    def __init__(self):
        super(ChuckNorris, self).__init__('Chuck Norris', False)
