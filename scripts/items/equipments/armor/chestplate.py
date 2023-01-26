from scripts.items.equipments.armor.armor import Armor


class Chestplate(Armor):
    def __init__(self, name, value, image, defense, quality):
        super().__init__(name, value, image, defense, quality)
        self.slot = "chestplate"