from Items.equipments.armor.armor import Armor


class Leggings(Armor):
    def __init__(self, name, value, image, defense, quality):
        super().__init__(name, value, image, defense, quality)
        self.slot = "leggings"