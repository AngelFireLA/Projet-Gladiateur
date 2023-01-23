from Items.item import Item
from Items.equipments.hand_held.weapons.weapon import Weapon


class Buster(Weapon):

    def __init__(self, name, value, image, damage: int, attack_speed: int, quality):
        super().__init__(name, value, image, damage, attack_speed, quality, 2)
        self.hands_used = 2